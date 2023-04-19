from pydantic import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    api_key: str = Field('', env='ELLIPTIC_API_KEY')
    api_secret: str = Field('', env='ELLIPTIC_API_SECRET')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
