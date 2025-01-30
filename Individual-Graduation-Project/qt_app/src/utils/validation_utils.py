from pydantic import BaseModel, EmailStr, ValidationError
from typing import Tuple

class User(BaseModel):
    email: EmailStr

def validate_user(email: str):
    try:
        User(email=email)
        return True
    except ValidationError:
        return False

def check_password(password: str) -> Tuple[bool, str]:
    if len(password) < 10:
        return False, "Слишком короткий пароль! минимум 10 символов"
    if not any(char.isdigit() for char in password):
        return False, "Пароль должен содержать хотя бы одну цифру!"
    if not any(char.isalpha() for char in password):
        return False, "Пароль должен содержать хотя бы одну букву!"
    if not any(char.isupper() for char in password):
        return False, "Пароль должен содержать хотя бы одну заглавную букву!"
    if not any(char.islower() for char in password):
        return False, "Пароль должен содержать хотя бы одну строчную букву!"
    return True, "Этот пароль надёжный!"