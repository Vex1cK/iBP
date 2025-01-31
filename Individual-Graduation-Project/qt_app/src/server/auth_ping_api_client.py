import logging
logger = logging.getLogger(__name__)

import requests
import time
from typing import Tuple
from pydantic import EmailStr

from src.config.config import SERVER_URL

def ping() -> Tuple[bool, str]:
    try:
        logger.debug("Пингуем сервер")
        start_time = time.time()
        response = requests.get(f"{SERVER_URL}/ping_time", params={"start_time": start_time}, timeout=2)
        assert response.status_code == 200
        latency = response.json()["latency_ms"]
        logger.debug(f"Задержка: {latency} мс")
        return True, str(latency)
    except Exception as e:
        logger.error(f"Ошибка при пинге сервера: {str(e)}")
        return False, str(e)

def login_request(email: EmailStr, password: str) -> Tuple[bool, str]:
    try:
        logger.debug("Отправляем запрос на авторизацию")
        response = requests.post(f"{SERVER_URL}/auth/login", json={"email": email, "password": password})
        if response.status_code == 200:
            logger.debug("Авторизация прошла успешно")
            return True, str(response.json()["access_token"])
        return False, response.json()["detail"]
    except Exception as e:
        logger.error(f"Ошибка при авторизации: {str(e)}")
        return False, str(e)

def logout(token: str) -> Tuple[bool, str]:
    try:
        logger.debug("Отправляем запрос на выход из аккаунта")
        response = requests.post(f"{SERVER_URL}/auth/logout", json={"access_token": token})
        if response.status_code == 200:
            logger.debug("Выход из аккаунта произошел успешно")
            return True, ""
        return False, response.json()["detail"]
    except Exception as e:
        logger.error(f"Ошибка при верификации токена: {str(e)}")
        return False, str(e)

def register_request(email: EmailStr, password: str) -> Tuple[bool, str]:
    try:
        logger.debug("Отправляем запрос на регистрацию")
        response = requests.post(f"{SERVER_URL}/auth/register", json={"email": email, "password": password})
        if response.status_code == 201:
            logger.debug("Аккаунт создан")
            # return True, str(response.json()["msg"])
            return True, "Аккаунт создан. Пожалуйста, проверьте почту,\nподтвердите свой email и войдите в аккаунт"
        return False, response.json()["detail"]
    except Exception as e:
        logger.error(f"Ошибка при регистрации: {str(e)}")
        return False, str(e)

def verify_token(token: str) -> bool:
    try:
        logger.debug("Отправляем запрос на проверку токена")
        response = requests.post(f"{SERVER_URL}/auth/verify-token", json={"access_token": token})
        if response.status_code == 200:
            logger.debug("Токен верифицирован")
            return True
        return False
    except Exception as e:
        logger.error(f"Ошибка при верификации токена: {str(e)}")
        return False

def update_token_in_auth_module():
    global SERVER_URL
    from src.config.config import SERVER_URL