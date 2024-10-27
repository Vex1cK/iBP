from random import choice
from enum import Enum
import datetime
import asyncio

class FileExtensions(str, Enum):
    txt = "txt"
    wav = "wav"


async def generate_unique_filename(extension: FileExtensions):
    """
    Возвращает уникальное имя файла на основе текущего времени.
    Имя файла будет формата: YYYYMMDD_HHMMSS_microseconds.<extension>
    Поддерживает Windows-совместимый формат имени.
    """
    now = datetime.datetime.now()
    number = choice(list(range(1, 10**6)))
    filename = now.strftime(f"%Y%m%d_%H%M%S_%f-{number}.{extension}")
    await asyncio.sleep(0)  # Асинхронная точка для имитации асинхронности
    return filename