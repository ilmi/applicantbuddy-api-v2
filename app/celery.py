from celery import Celery

from app.core.settings import settings

app = Celery("tasks", broker=settings.database_settings.REDIS_URL, backend=settings.database_settings.REDIS_URL)

# Configure autodiscovery
app.conf.update(include=["app.services.resume.task", "app.services.vacancies.linkedin_scrapper_task"])
