from typing import List

from fastapi import APIRouter
from app.db.emulate_db import get_cameras_data_from_db
from app import schemas

router = APIRouter()


@router.get("/get-all-cameras", response_model=List[schemas.CameraBase])
async def get_all_cameras() :
    """
    Возвращает данные о камерах.
    """
    return await get_cameras_data_from_db()
