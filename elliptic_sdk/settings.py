"""Elliptic SDK elliptic_sdk/settings.py."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings."""

    api_key: str
    api_secret: str

    class Config:
        """Config."""

        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'ELLIPTIC_'


settings = Settings()
