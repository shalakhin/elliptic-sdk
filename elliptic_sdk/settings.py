"""Elliptic SDK elliptic_sdk/settings.py."""
from pydantic import BaseSettings

TIMEOUT_DEFAULT = 5


class Settings(BaseSettings):
    """Settings."""

    api_key: str
    api_secret: str
    timeout: float = TIMEOUT_DEFAULT

    class Config:
        """Config."""

        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'ELLIPTIC_'


settings = Settings()
