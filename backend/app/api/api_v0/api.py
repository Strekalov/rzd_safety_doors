from fastapi import APIRouter

from app.api.api_v0.endpoints import cameras, analysis

api_router = APIRouter()
api_router.include_router(cameras.router, prefix="/cameras", tags=["cameras"])
api_router.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
