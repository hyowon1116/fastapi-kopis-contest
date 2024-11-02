from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    KOPISSERVICEKEY:str
    
    model_config = SettingsConfigDict(env_file=".env")