import logging
from config import loggers_level

logging.basicConfig(
    level=loggers_level,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

logger.debug("Импортируем сторонние модули")
from contextlib import asynccontextmanager
from sqlalchemy.exc import OperationalError
from fastapi import FastAPI
from sqlalchemy import text
import asyncio
import uvicorn
import os

logger.debug("Импортируем внутренние модули")

from config import paths_need_to_check, paths_to_models_to_check

logger.debug("Проверяем наличие всех нужных директорий")
for path_to_check in paths_need_to_check:
    try:
        logger.debug(f"Checking path: {path_to_check}")
        if not os.path.exists(path_to_check):
            logger.debug("Path does not exist")
            logger.debug("Creating path")
            os.mkdir(path_to_check)
            if os.path.exists(path_to_check):
                logger.debug("Path created")
                continue
            logger.error("Failed to create audio path")
            logger.error("Exiting the program")
            raise Exception("Я хз че там произошло")
        logger.debug("Path exists")
    except Exception as e:
        # logging.error("Failed to create audio path: " + str(e))
        logger.error(f"Failed to create dir {path_to_check}: " + str(e))
        exit(1)

for path_to_check in paths_to_models_to_check:
    try:
        logger.debug(f"Checking model: {path_to_check}")
        if not os.path.exists(path_to_check):
            os.makedirs(path_to_check, exist_ok=True)
        if os.listdir(path_to_check) == []:
            logger.error(f"Модель по пути {path_to_check} не найдена! Проверьте файлы проекта, или попробуйте запуститься из докер контейнера.")  # noqa: E501
            exit(1)
        logger.debug(f"Файлы модели {path_to_check} найдены")
    except Exception as e:
        logger.error(f"Failed to create dir {path_to_check}: " + str(e))
        exit(1)

from database import async_session_factory
from all_routers import all_routers

from auth.email_services import init_smtp_client, close_smtp_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    if os.getenv("TESTING", False):
        yield
    else:
        await init_smtp_client()
        logger.debug("SMTP client initialized")
        yield
        await close_smtp_client()
        logger.debug("SMTP client closed")

app = FastAPI(title="GOL", lifespan=lifespan)

smtp_client = None

logger.debug("Подключаем роутеры")

for router in all_routers:
    app.include_router(router)


async def get_sqlite_version() -> tuple[bool, str]:
    try:
        async with async_session_factory() as session:
            result = await session.execute(text("SELECT sqlite_version();"))
            version = result.scalar()
            return True, version
    except OperationalError as e:
        return False, f"An error occurred: {e}"

def main():
    logger.debug("Получаем версию SQLite")
    status, message = asyncio.run(get_sqlite_version())
    if status:
        logger.info(f"SQLite version: {message}")
        uvicorn.run(app, host="localhost", port=8000, log_level=loggers_level)
    else:
        logger.error(message)
        return 1


if __name__ == "__main__":
    logger.info("Запускаемси")
    status = main()
    if status != 0:
        exit(status)
