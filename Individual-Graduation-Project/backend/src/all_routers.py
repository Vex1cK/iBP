from auth.router import router as auth_router
from ML_api.router import router as ml_router
from root_router.router import router as root_router

all_routers = [
    root_router,
    auth_router,
    ml_router,
]