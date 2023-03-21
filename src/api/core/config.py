import os
from pathlib import Path

from dotenv import load_dotenv

# env_dir_path = (Path(__file__)/"..").resolve()
#
# path_env_file = os.path.join(env_dir_path, ".env")

load_dotenv()


class Settings:
    APP_TITLE: str = os.getenv("APP_TITLE")
    VERSION: int = os.getenv("VERSION")
    HOST: str = os.getenv("HOST")
    PORT: int = os.getenv("PORT")


settings = Settings()


