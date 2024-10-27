import logging
logger = logging.getLogger(__name__)

from fastapi import APIRouter
from fastapi.responses import FileResponse, JSONResponse

from config import ICO_PATH

logger.debug("Создаём root router")

router = APIRouter()

@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(ICO_PATH)

@router.get("/")
async def home_page():
    return JSONResponse(content={"msg": "Hello Yopta"}, status_code=200)