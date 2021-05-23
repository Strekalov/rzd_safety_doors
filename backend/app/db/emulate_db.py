from app.core import settings
import json 
import aiofiles


async def get_cameras_data_from_db():
    "Эмулируем получение данных из БД."
    async with aiofiles.open(f"{settings.DEMO_DATA_DIR}/cameras.json") as file:
        json_file = await file.read()
    return json.loads(json_file)
