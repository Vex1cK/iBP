from sqlalchemy import select
from httpx import AsyncClient

from .config_for_tests import async_session_maker_test

from src import User


async def test_add_user(ac: AsyncClient):
    response = await ac.post("/auth/register", json={"email": "user_add@example.com", "password": "password123add"})
    assert response.status_code == 201

    async with async_session_maker_test() as session:
        query = select(User).where(User.email == "user_add@example.com")
        result = await session.execute(query)
        user = result.scalar()
        assert user.email == "user_add@example.com", "Пользователь не добавился"
        assert user.is_verified == False
        assert user.hashed_password != "password123add"
