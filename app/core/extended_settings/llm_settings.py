from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    OPENAI_API_KEY: str = "sk-not-provided"
    OPENAI_BASE_URL: str = "https://openrouter.ai/api/v1"
    MISTRAL_API_KEY: str = "sk-not-provided"
    TAVILY_API_KEY: str = "tvly-not-provided"
