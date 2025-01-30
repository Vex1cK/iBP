import logging
logger = logging.getLogger(__name__)

from fastapi import UploadFile
import aiofiles
import os
from typing import Tuple, Optional

from .utils_ml import generate_unique_filename

async def create_and_write_file(content: bytes, extension: str, path_to_save: str):
    file_name = await generate_unique_filename(extension=extension)
    file_path = os.path.join(path_to_save, file_name)
    async with aiofiles.open(file_path, "wb") as buffer:
        await buffer.write(content)

    return file_name, file_path

def check_file_isnt_empty_and_good(file: UploadFile) -> Tuple[bool, Optional[bytes]]:
    try:
        content = file.file.read()
        if len(content) == 0:
            return False, None
        return True, content
    except Exception:
        return False, None