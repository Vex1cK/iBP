import logging
logger = logging.getLogger(__name__)

from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext
import asyncio
from typing import Tuple, Optional, Dict, Any

from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from auth.models import Token, User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

async def decode_access_token_async(token: str) -> Optional[Dict[str, Any]]:
    loop = asyncio.get_event_loop()
    try:
        payload = await loop.run_in_executor(None, jwt.decode, token, SECRET_KEY, [ALGORITHM])
        return payload
    except JWTError:
        return None

async def verify_password_async(plain_password: str, hashed_password: str) -> bool:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, pwd_context.verify, plain_password, hashed_password)

async def get_password_hash_async(password: str) -> str:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, pwd_context.hash, password)

async def create_access_token_async(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    loop = asyncio.get_event_loop()
    encoded_jwt = await loop.run_in_executor(None, jwt.encode, to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt

async def check_token(token: str, session: AsyncSession) -> Tuple[int, str]:
    # logger.debug(f"Check token {token=}")
    token_data = await decode_access_token_async(token)
    # logger.debug(f"Token data: {token_data=}")
    if not token_data:
        return 401, "Invalid token"
    
    result = await session.execute(select(Token).where(Token.token == token))
    token_db: Token = result.scalars().first()
    if token_db:
        return 401, "Invalid token"
    
    user_email = token_data.get("sub")
    if not user_email:
        return 401, "Invalid token"

    result = await session.execute(select(User).where(User.email == user_email))
    user = result.scalars().first()
    if not user:
        return 401, "User not found"
    
    return 200, "OK"