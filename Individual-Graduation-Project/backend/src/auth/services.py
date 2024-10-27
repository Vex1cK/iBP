import logging
logger = logging.getLogger(__name__)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Tuple, Optional
from pydantic import EmailStr

from utils import (get_password_hash_async, create_access_token_async, decode_access_token_async)

from .models import User, Token

async def check_user_already_registered(user_email: EmailStr, session: AsyncSession) -> Tuple[bool, Optional[User]]:
    result = await session.execute(select(User).where(User.email == user_email))
    user: User = result.scalars().first()
    if bool(user):
        return True, user
    return False, None

async def check_user_is_verified(user_email: EmailStr, session: AsyncSession) -> Tuple[bool, Optional[User]]:
    registered, user = await check_user_already_registered(user_email, session)
    if not registered:
        return False, user
    return bool(user.is_verified), user

async def add_user_into_db(user_email: EmailStr, user_password: str, session: AsyncSession) -> User:
    hashed_password = await get_password_hash_async(user_password)

    new_user = User(email=user_email, hashed_password=hashed_password)

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return new_user

async def generate_token_for_user(user_email: EmailStr) -> str:
    access_token = await create_access_token_async(data={"sub": user_email})
    return access_token


async def ban_token(token: str, session: AsyncSession) -> Tuple[int, str]:
    token_data = await decode_access_token_async(token)
    
    user_email = token_data["sub"]

    registered, user = await check_user_already_registered(user_email, session)
    if not registered:
        return 404, "User not found"

    new_token = Token(user_id=user.id, token=token)
    session.add(new_token)
    await session.commit()

    return 200, "Logged out successfully"

async def verify_email_service(token: str, session: AsyncSession):
    token_data = await decode_access_token_async(token)
    
    user_email = token_data["sub"]

    registered, user = await check_user_already_registered(user_email, session)
    if not registered:
        return 404, "User not found"
    
    user.is_verified = True
    await session.commit()

    return 200, "Email verified"