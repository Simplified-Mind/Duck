from fastapi import APIRouter
from backend.app.api.endpoints.commodity import environmental, lng, gas, power


api_router = APIRouter()


# ------------------ Commodity ------------------
# Environmental
api_router.include_router(
    environmental.fundamental.router,
    prefix='/environmental/fundamental',
    tags=['Environmental']
)

# Gas
api_router.include_router(
    gas.fundamental.router,
    prefix='/gas/fundamental',
    tags=['Gas']
)

# LNG
api_router.include_router(
    lng.fundamental.router,
    prefix='/lng/fundamental',
    tags=['LNG']
)

# Power
api_router.include_router(
    power.fundamental.router,
    prefix='/power/fundamental',
    tags=['Power']
)
