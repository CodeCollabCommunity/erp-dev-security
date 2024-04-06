"""
Base settings for all apps
"""
# from pydantic import Extra
from pydantic_settings import BaseSettings
import os
CONFIG_FILE = ".env"


class AppSettings(BaseSettings):
    #: The application domain
    API_DOMAIN: str = os.getenv("API_DOMAIN")

    class Config:
        env_file = CONFIG_FILE
        # extra = Extra.forbid
        extra = "allow"


class Settings(BaseSettings):
    #: The application domain
    API_DOMAIN: str = os.getenv("API_DOMAIN")

