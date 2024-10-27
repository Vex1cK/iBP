from sqlalchemy.future import select
from pydantic import EmailStr

from src import User

from .config_for_tests import async_session_maker_test


async def verify_users_email(user_email: EmailStr) -> bool:
    async with async_session_maker_test() as session:
        result = await session.execute(select(User).where(User.email == user_email))
        user: User = result.scalars().first()
        if user:
            user.is_verified = True
            await session.commit()
            return True
        return False