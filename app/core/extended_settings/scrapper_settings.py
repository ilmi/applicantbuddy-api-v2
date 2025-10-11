from pydantic_settings import BaseSettings, SettingsConfigDict


class ScrapperSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore")

    LINKEDIN_SCRAPPER_KEY: str = ""
