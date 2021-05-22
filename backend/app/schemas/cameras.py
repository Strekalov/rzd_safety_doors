from pydantic import BaseModel


class CameraBase(BaseModel):
    camera_number: str
    title: str
    screen_url: str

