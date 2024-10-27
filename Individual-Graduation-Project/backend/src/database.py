from config import DB_NAME
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator
import os

here = os.getcwd()
DB_PATH = os.path.join(here, DB_NAME)
DB_URL = f"sqlite+aiosqlite:///{DB_PATH}"
async_engine = create_async_engine(DB_URL)
async_session_factory = async_sessionmaker(async_engine)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session

class Base(DeclarativeBase):
    pass