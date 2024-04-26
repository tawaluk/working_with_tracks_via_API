import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):

    DB_HOST: str = os.getenv("DB_HOST", default="tawaluk.ru")
    DB_PORT: str = os.getenv("DB_PORT", default="5432")
    DB_USER: str = os.getenv("DB_USER", default="tawaluk")
    DB_PASS: str = os.getenv("DB_PASS", default="1microlab")
    DB_NAME: str = os.getenv("DB_NAME", default="tawaluk")

    @property
    def database_url_async_psycopg(self):
        return (
            f"postgresql+psycopg2://{self.DB_USER}:"
            f"{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
