from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app import schemas

router = APIRouter()


@router.get("/get-all-cameras", response_model=List[schemas.CameraBase])
def read_items() :
    """
    Retrieve items.
    """
    return [{"camera_number": 1, "title": "Камера 1", "screen_url": "url1"}, 
            {"camera_number": 2, "title": "Камера 2", "screen_url": "url2"}]
