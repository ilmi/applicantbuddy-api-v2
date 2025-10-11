from mistralai import Mistral
from openai import OpenAI
from tavily import TavilyClient

from app.core.settings import settings

openai_client = OpenAI(
    api_key=settings.llm_settings.OPENAI_API_KEY,
)
mistral_client = Mistral(api_key=settings.llm_settings.MISTRAL_API_KEY)
tavily_client = TavilyClient(api_key=settings.llm_settings.TAVILY_API_KEY)
