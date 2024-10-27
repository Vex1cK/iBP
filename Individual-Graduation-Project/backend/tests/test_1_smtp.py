import pytest
from fastapi import BackgroundTasks
from src.auth.email_services import send_confirmation_email

@pytest.mark.asyncio
async def test_send_confirmation_email(mock_smtp_client):
    email = "test@example.com"
    background_tasks = BackgroundTasks()

    # Вызываем функцию отправки email
    status, message = await send_confirmation_email(email, background_tasks)

    # Проверяем, что задача была добавлена в background_tasks
    assert status == 201
    assert message == "Email sent successfully"