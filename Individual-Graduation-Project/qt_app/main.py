import logging
from src.config.config import (loggers_level, NONE_VALUE, 
                               USER_TOKEN, HAVE_TOKEN, 
                               AUDIO_PATH, FULL_TEXT_PATH, 
                               SUM_TEXT_PATH, FOLDER_PATH)
paths = [AUDIO_PATH, FULL_TEXT_PATH, SUM_TEXT_PATH, FOLDER_PATH]

logging.basicConfig(
    level=loggers_level,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

from src.config.COM_init import result  # noqa: F401  # type: ignore

import sys
import os

from PySide6.QtWidgets import QApplication

from src.server.auth_ping_api_client import ping, verify_token
from src.windows.main_windows import MainApp
from src.utils.other_utils import update_token_in_json_and_config

def check_paths():
    for path in paths:
        if not os.path.exists(path):
            logger.info(f"Path {path} does not exist")
            logger.debug("Creating path")
            os.mkdir(path)
            if os.path.exists(path):
                logger.debug("Path created")
                continue
            logger.error(f"Failed to create {path}")
            logger.error("Exiting the program")
            exit(1)

def main():
    logger.debug("Начало работы")

    check_paths()

    ping_ok, ping_msg = ping()

    if not ping_ok:
        logger.error("Сервер не доступен")
    else:
        logger.info(f"Сервер доступен. ping: {round(float(ping_msg), 1)} ms")
    
    if HAVE_TOKEN and ping_ok:
        ok = verify_token(USER_TOKEN)
        if not ok:
            update_token_in_json_and_config(NONE_VALUE)
    
    logger.debug("Создаём QApplication")
    app = QApplication(sys.argv)
    logger.debug(f"{app=}")
    logger.debug("Создаём объект приложения")
    window = MainApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()