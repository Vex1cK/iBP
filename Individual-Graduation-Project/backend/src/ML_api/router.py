import logging
logger = logging.getLogger(__name__)

from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
import os

from utils import (credentials_exception, check_token)
from database import get_async_session

from .services import create_and_write_audio_file
from .audio2text import AudioToTextAsync

from auth.schemas import TokenData

logger.debug("Создаём ML роутер")

router = APIRouter(prefix='/ml')
audio_processor = AudioToTextAsync()

@router.post("/transcribe_audio")
async def transcribe_audio(access_token: str,
                            file: UploadFile = File(...),
                            session: AsyncSession = Depends(get_async_session)):

    status, msg = await check_token(access_token, session)

    if status != 200:
        if status == 401:
            raise credentials_exception
        logger.warning("Странный статус код")
        raise HTTPException(status_code=status, detail=msg)

    file_name, file_path = await create_and_write_audio_file(file)

    success, output_path = await audio_processor.transcribe_audio(file_path, file_name.replace(".wav", ".txt"))

    logger.debug("Удаляем использованный аудио файл пользователя")
    os.remove(file_path)

    if not success:
        logger.error("Не удалось протранскрайбить аудио")
        raise HTTPException(status_code=500)

    return FileResponse(output_path)
    