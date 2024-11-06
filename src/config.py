from functools import lru_cache
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    KOPISSERVICEKEY:str
    SECRET_KEY:Optional[str]=None
    DATABASE_FILE:Optional[str]=None
    JOBSERVICEKEY:Optional[str]=None

    
    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings():
    return Settings()


