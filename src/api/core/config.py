from dotenv import load_dotenv
from pathlib import Path
import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    class Settings:
        APP_TITLE: str = os.getenv("APP_TITLE")
        VERSION: int = os.getenv("VERSION")
        HOST: str = os.getenv("HOST")
        PORT: int = os.getenv("PORT")

    class Config:
        env_file = ".env"

# env_dir_path = (Path(__file__)/".."/"..").resolve()
#
# path_env_file = os.path.join(env_dir_path, ".env")
#
# load_dotenv(dotenv_path=path_env_file)
#
#
# class Settings:
#     APP_TITLE: str = "My APP....." #os.getenv("APP_TITLE")
#     VERSION: int = 1.0 ##os.getenv("VERSION")
#     HOST: str = "0.0.0.0" ###os.getenv("HOST")
#     PORT: int = 8081 ##os.getenv("PORT")
#

settings = Settings()


