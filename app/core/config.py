from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Production Cockpit"
    API_V1_URI: str = "/api/v1"
    MONGODB_DSN: str
    MONGODB_DB: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
