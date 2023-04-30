"""Elliptic SDK elliptic_sdk/settings.py."""
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Settings."""

    api_key: str = Field(env='ELLIPTIC_API_KEY')
    api_secret: str = Field(env='ELLIPTIC_API_SECRET')

    class Config:
        """Config."""

        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
