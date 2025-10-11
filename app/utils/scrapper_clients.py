from apify_client import ApifyClient

from app.core.settings import settings

linkedin_client = ApifyClient(token=settings.scrapper_settings.LINKEDIN_SCRAPPER_KEY)
