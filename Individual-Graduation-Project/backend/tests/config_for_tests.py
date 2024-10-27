import os
from src.config import DB_NAME_TEST
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from typing import AsyncGenerator

here = os.getcwd().replace('\\', '/')
DATABASE_URL_TEST = "sqlite+aiosqlite:///" + here + f"/tests/{DB_NAME_TEST}"

engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool, echo=False)
async_session_maker_test = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)

PATH_TO_TEST_FILES = os.path.join(here, "tests", "test_files")

async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker_test() as session:
        yield session