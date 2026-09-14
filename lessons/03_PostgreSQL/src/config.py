from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

# определяем абсолютный путь до корня проекта
BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    DB_NAME: str 
    # DB_NAME: str | None = None
    # если в переменной окружения нет DB_NAME - присваиваем значение None
    # !!! НО !!! 
    # так мы делаем, т.к. мы всегда ожидаем вхождение переменных окружения

    model_config = SettingsConfigDict(env_file=".env")
    # model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    # extra="ignore" - игнорируем недостающие или дополнительные переменные в файле


settings = Settings()