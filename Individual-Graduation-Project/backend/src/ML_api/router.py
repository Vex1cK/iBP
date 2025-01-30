import logging
logger = logging.getLogger(__name__)

from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
import os

from utils import (credentials_exception, check_token)
from database import get_async_session
from config import PATH_TO_USERS_AUDIO_FILES, PATH_TO_USERS_TXT_FILES

from .services import create_and_write_file, check_file_isnt_empty_and_good
from .audio2text import AudioToTextAsync
from .text2text_sum import SummarizerAsync

logger.debug("Создаём ML роутер")

router = APIRouter(prefix='/ml')
audio_processor = AudioToTextAsync()
summarizer = SummarizerAsync()


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

    ok, content = check_file_isnt_empty_and_good(file)

    if not ok:
        logger.error("Пустой файл или что-то не так с файлом")
        raise HTTPException(status_code=400, detail="Пустой файл или что-то не так с файлом")

    file_name, file_path = await create_and_write_file(content, 'wav', PATH_TO_USERS_AUDIO_FILES)

    success, output_path = await audio_processor.transcribe_audio(file_path, file_name.replace(".wav", ".txt"))

    logger.debug("Удаляем использованный аудио файл пользователя")
    os.remove(file_path)

    if not success:
        logger.error("Не удалось протранскрайбить аудио")
        raise HTTPException(status_code=500)

    return FileResponse(output_path)


@router.post("/sum_text")
async def sum_text(access_token: str,
                   file: UploadFile = File(...),
                   session: AsyncSession = Depends(get_async_session)):

    status, msg = await check_token(access_token, session)

    if status != 200:
        if status == 401:
            raise credentials_exception
        logger.warning("Странный статус код")
        raise HTTPException(status_code=status, detail=msg)

    ok, content = check_file_isnt_empty_and_good(file)

    if not ok:
        logger.error("Пустой файл или что-то не так с файлом")
        raise HTTPException(status_code=400, detail="Пустой файл или что-то не так с файлом")

    file_name, file_path = await create_and_write_file(content, 'txt', PATH_TO_USERS_TXT_FILES)

    success, output_path = await summarizer.summarize_text(file_path, "sum " + file_name)

    logger.debug("Удаляем использованный текстовый файл пользователя")
    os.remove(file_path)

    if not success:
        logger.error("Не удалось суммаризировать текст")
        raise HTTPException(status_code=500)

    return FileResponse(output_path)