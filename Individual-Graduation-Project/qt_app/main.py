import logging
from src.config.config import loggers_level, NONE_VALUE, USER_TOKEN, HAVE_TOKEN

logging.basicConfig(
    level=loggers_level,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

from src.config.COM_init import result  #noqa  #type: ignore

import sys
from PySide6.QtWidgets import QApplication

from src.server.auth_ping_api_client import ping, verify_token
from src.windows.main_windows import MainApp
from src.utils.other_utils import update_token_in_json_and_config

def main():
    logger.debug("Начало работы..")

    ping_ok, _ = ping()

    if not ping_ok:
        logger.error("Сервер не доступен")
    
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