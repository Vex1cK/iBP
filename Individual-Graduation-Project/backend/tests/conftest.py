from typing import AsyncGenerator

import pytest
from httpx import AsyncClient, ASGITransport
from database import get_async_session  # type: ignore
from src import Base
from src.main import app
from .config_for_tests import override_get_async_session, engine_test
from unittest.mock import AsyncMock
import os

app.dependency_overrides[get_async_session] = override_get_async_session

@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture(scope="session", autouse=True)
def set_testing_env():
    os.environ["TESTING"] = "1"
    yield
    del os.environ["TESTING"]

@pytest.fixture(scope="function", autouse=True)
def mock_smtp_client(monkeypatch):
    mock_smtp = AsyncMock()
    
    monkeypatch.setattr("src.auth.email_services.smtp_client", mock_smtp)
    
    monkeypatch.setattr("src.auth.email_services.init_smtp_client", AsyncMock())
    monkeypatch.setattr("src.auth.email_services.close_smtp_client", AsyncMock())

    return mock_smtp

@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
