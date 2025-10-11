from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    APP_NAME: str = "Applicant Buddy API"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "API for Applicant Buddy"

    DEBUG: bool = False

    ALLOW_ORIGINS: list[str] = ["*"]
    ALLOW_METHODS: list[str] = ["*"]
    ALLOW_HEADERS: list[str] = ["*"]

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
