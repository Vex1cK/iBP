import logging
logger = logging.getLogger(__name__)

from fastapi import UploadFile
import os

from config import PATH_TO_USERS_AUDIO_FILES

from .utils_ml import generate_unique_filename

async def create_and_write_audio_file(file: UploadFile):
    file_name = await generate_unique_filename(extension='wav')
    file_path = os.path.join(PATH_TO_USERS_AUDIO_FILES, file_name)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    
    return file_name, file_path