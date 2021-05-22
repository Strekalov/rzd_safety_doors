from fastapi import APIRouter

from app.api.api_v0.endpoints import cameras

api_router = APIRouter()
api_router.include_router(cameras.router, prefix="/cameras", tags=["cameras"])

