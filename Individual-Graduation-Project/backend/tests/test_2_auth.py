from httpx import AsyncClient

from .utils_for_tests import verify_users_email

# Тест регистрации нового пользователя
async def test_register(ac: AsyncClient):
    response = await ac.post("/auth/register", json={"email": "user1@example.com", "password": "password123"})
    assert response.status_code == 201

# Тест регистрации нового пользователя с невалидным email
async def test_register_invalid_email(ac: AsyncClient):
    response = await ac.post("/auth/register", json={"email": "invalidemail", "password": "password123"})
    assert response.status_code == 422

# Тест на проверку, что нельзя зарегистрировать пользователя с уже существующим email
async def test_register_existing_email(ac: AsyncClient):
    # Зарегистрируем первого пользователя
    await ac.post("/auth/register", json={"email": "user2@example.com", "password": "password123"})
    # Пытаемся зарегистрировать пользователя с таким же email
    response = await ac.post("/auth/register", json={"email": "user2@example.com", "password": "password456"})
    assert response.status_code == 409
    assert response.json() == {"detail": "Email already registered"}

# Тест успешной авторизации
async def test_login(ac: AsyncClient):
    # Сначала нужно зарегистрировать пользователя
    await ac.post("/auth/register", json={"email": "user3@example.com", "password": "password123"})
    
    # потом верифицировать email, сделаем это в лоб
    ok = await verify_users_email("user3@example.com")
    assert ok

    # Теперь проверим авторизацию
    response = await ac.post("/auth/login", json={"email": "user3@example.com", "password": "password123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

# Тест неудачной авторизации (неправильный email или пароль)
async def test_login_invalid_credentials(ac: AsyncClient):
    response = await ac.post("/auth/login", json={"email": "invalid@example.com", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}

async def test_login_invalid_email_form(ac: AsyncClient):
    response = await ac.post("/auth/login", json={"email": "invalidemail", "password": "password123"})
    assert response.status_code == 422

# Тест выхода из аккаунта (logout)
async def test_logout_ang_logout_with_banned_token(ac: AsyncClient):
    # Регистрация пользователя
    register_response = await ac.post("/auth/login", json={"email": "user3@example.com", "password": "password123"})
    access_token = register_response.json()["access_token"]

    # Логаут
    response = await ac.post("/auth/logout", json={"access_token": access_token})
    assert response.status_code == 200
    assert response.json() == {"msg": "Logged out successfully"}

    # Логаут с забаненым токеном
    response = await ac.post("/auth/logout", json={"access_token": access_token})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid token"}


# Тест логаута с невалидным токеном
async def test_logout_invalid_token(ac: AsyncClient):
    response = await ac.post("/auth/logout", json={"access_token": "invalidtoken"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid token"}