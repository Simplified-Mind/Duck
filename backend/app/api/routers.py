from fastapi import APIRouter
from backend.app.api.endpoints.commodity.environmental import fundamental as environmental_fundamental
from backend.app.api.endpoints.commodity.gas import fundamental as gas_fundamental
from backend.app.api.endpoints.commodity.lng import fundamental as lng_fundamental
from backend.app.api.endpoints.commodity.power import fundamental as power_fundamental


api_router = APIRouter()


# ------------------ Commodity ------------------
# Environmental
api_router.include_router(
    environmental_fundamental.router,
    prefix='/environmental',
    tags=['Environmental']
)

# Gas
api_router.include_router(
    gas_fundamental.router,
    prefix='/gas',
    tags=['Gas']
)

# LNG
api_router.include_router(
    lng_fundamental.router,
    prefix='/lng',
    tags=['LNG']
)

# Power
api_router.include_router(
    power_fundamental.router,
    prefix='/power',
    tags=['Power']
)
