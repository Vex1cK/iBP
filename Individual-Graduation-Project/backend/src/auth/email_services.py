import logging
logger = logging.getLogger(__name__)

from email.message import EmailMessage
from fastapi import BackgroundTasks
from unittest.mock import AsyncMock
from pydantic import EmailStr
from datetime import timedelta
import aiosmtplib
import os

from config import SMTP_EMAIL, FRONTEND_URL, SMTP_PASSWORD, SMTP_HOSTNAME, SMTP_PORT
from utils import create_access_token_async

smtp_client = None

async def init_smtp_client():
    global smtp_client
    smtp_client = aiosmtplib.SMTP(hostname=SMTP_HOSTNAME, port=SMTP_PORT)
    await smtp_client.connect()
    # await smtp_client.starttls()
    await smtp_client.login(SMTP_EMAIL, SMTP_PASSWORD)
    # logger.debug(f"SMTP client (init): {smtp_client}, {type(smtp_client)}")


async def close_smtp_client():
    global smtp_client
    # logger.debug(f"SMTP client (closing): {smtp_client}, {type(smtp_client)}")
    if smtp_client:
        await smtp_client.quit()

async def send_email_async(recipient: EmailStr, subject: str, body: str):
    global smtp_client
    message = EmailMessage()
    message["From"] = SMTP_EMAIL
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if bool(os.getenv("TESTING")):
        smtp_client = AsyncMock()

    await smtp_client.send_message(message)

async def send_confirmation_email(email: str, background_tasks: BackgroundTasks):
    token = await create_access_token_async(data={"sub": email}, expires_delta=timedelta(hours=1))
    confirm_url = f"{FRONTEND_URL}/auth/verify-email?token={token}"  # Генерация ссылки для подтверждения

    subject = "Подтверждение вашего email"
    body = f"Здравствуйте!\n\nДля подтверждения вашего email перейдите по ссылке: {confirm_url}\n\nЕсли вы не регистрировались, просто проигнорируйте это письмо."

    background_tasks.add_task(send_email_async, email, subject, body)

    return 201, "Email sent successfully"