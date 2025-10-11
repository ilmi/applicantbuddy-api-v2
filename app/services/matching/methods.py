from typing import List

from loguru import logger
from sqlmodel import Session, desc, select

from app.database.engine import engine
from app.database.models import JobVacancies, Resume


def find_suitable_jobs() -> List[JobVacancies]:
    with Session(engine) as session:
        latest_resume_stmt = select(Resume).order_by(desc(Resume.updated_at)).limit(1)
        latest_resume = session.exec(latest_resume_stmt).first()

        if not latest_resume or not latest_resume.category:
            logger.warning("No resume found or resume has no category")
            return []

        category = latest_resume.category.replace("_", " ")
        logger.info(f"Searching jobs for category: {category}")

        if not category:
            logger.warning("Your CV is not categorized. Please update with better resume format.")
            return []

        job_stmt = (
            select(JobVacancies)
            .where(JobVacancies.title.ilike(f"%{category}%"))  # type: ignore
            .order_by(desc(JobVacancies.created_at))
        )
        matching_jobs = session.exec(job_stmt).all()

        logger.info(f"Found {len(matching_jobs)} matching jobs")
        return list(matching_jobs)
