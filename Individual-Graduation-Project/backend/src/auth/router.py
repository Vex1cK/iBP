import logging
logger = logging.getLogger(__name__)

from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from utils import (check_token, verify_password_async)
from database import get_async_session

from .schemas import UserCreate, UserLogin, TokenData
from .services import (check_user_already_registered, add_user_into_db, generate_token_for_user,
                       check_user_is_verified, ban_token, verify_email_service)
from .email_services import send_confirmation_email

router = APIRouter(prefix="/auth")

@router.post("/register", response_model=TokenData)
async def register(user_data: UserCreate, background_tasks: BackgroundTasks, session: AsyncSession = Depends(get_async_session)):
    ok, _ = await check_user_already_registered(user_data.email, session)
    
    if ok:
        raise HTTPException(status_code=409, detail="Email already registered")

    new_user = await add_user_into_db(user_data.email, user_data.password, session)

    status, msg = await send_confirmation_email(new_user.email, background_tasks)

    if status != 201:
        raise HTTPException(status_code=status, detail=msg)

    return JSONResponse(content={"msg": "User created. Please check and verify your email"}, status_code=201)

@router.post("/login", response_model=TokenData)
async def login(user_data: UserLogin, session: AsyncSession = Depends(get_async_session)):
    ok, user = await check_user_is_verified(user_data.email, session)

    if not ok and not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    elif not ok:
        raise HTTPException(status_code=403, detail="Email is not verified")
    else:
        if not await verify_password_async(user_data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        access_token = await generate_token_for_user(user.email)

        return JSONResponse(content={"access_token": access_token, "token_type": "bearer"}, status_code=200)

@router.post("/logout")
async def logout(token: TokenData, session: AsyncSession = Depends(get_async_session)):
    
    status, msg = await check_token(token.access_token, session)

    if status != 200:
        if status != 401:
            logger.warning("Странный статус код")
        raise HTTPException(status_code=status, detail=msg)

    status, msg = await ban_token(token.access_token, session)
    
    if status != 200:
        raise HTTPException(status_code=status, detail=msg)
    return JSONResponse(status_code=status, content={'msg': msg})


@router.get("/verify-email")
async def verify_email(token: str, session: AsyncSession = Depends(get_async_session)):
    status, msg = await check_token(token, session)

    if status != 200:
        if status != 401:
            logger.warning("Странный статус код")
        raise HTTPException(status_code=status, detail=msg)
    
    status, msg = await verify_email_service(token, session)

    if status != 200:
        raise HTTPException(status_code=status, detail=msg)
    return JSONResponse(status_code=status, content={'msg': msg})