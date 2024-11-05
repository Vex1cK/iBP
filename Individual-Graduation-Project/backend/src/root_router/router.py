import logging
logger = logging.getLogger(__name__)

from fastapi import APIRouter
from fastapi.responses import FileResponse, JSONResponse
import time

from config import ICO_PATH

logger.debug("Создаём root router")

router = APIRouter()

@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(ICO_PATH)

@router.get("/")
async def home_page():
    return JSONResponse(content={"msg": "Hello there"}, status_code=200)

@router.get("/ping", response_class=JSONResponse)
async def ping():
    return JSONResponse(content={"message": "pong"}, status_code=200)

@router.get("/ping_time", response_class=JSONResponse)
async def ping_time(start_time: float):
    end_time = time.time()
    
    latency_ms = (end_time - start_time) * 1000
    return JSONResponse(content={"message": "pong", "latency_ms": latency_ms}, status_code=200)