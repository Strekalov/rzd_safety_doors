from fastapi import FastAPI

from app.api.api_v0.api import api_router
from app.core import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V0_STR}/openapi.json"
)


app.include_router(api_router, prefix=settings.API_V0_STR)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)