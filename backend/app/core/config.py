from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "API для сервиса Safety Doors."
    API_V0_STR: str = "/api/v0"


settings = Settings()