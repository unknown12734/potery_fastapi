import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_TITLE: str = os.getenv("APP_TITLE")
    VERSION: int = os.getenv("VERSION")
    # HOST: str = os.getenv("HOST")
    # PORT: int = os.getenv("PORT")


settings = Settings()


