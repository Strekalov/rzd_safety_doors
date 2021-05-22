import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
PROJECT_NAME: str = "API для сервиса Safety Doors."
API_V0_STR: str = "/api/v0"

DEMO_DATA_DIR = f"{BASE_DIR}/hardcode_data"

