from typing import List

from loguru import logger
from sqlmodel import Session, desc, select

from app.database.engine import engine
from app.database.models import JobVacancies, Resume, ResumeStatus


def find_suitable_jobs(resume_id: str) -> List[JobVacancies]:
    with Session(engine) as session:
        resume_stmt = select(Resume).where(Resume.id == resume_id)
        resume = session.exec(resume_stmt).first()

        if not resume:
            logger.warning(f"No resume found with id: {resume_id}")
            return []
        
        if resume.status != ResumeStatus.COMPLETED:
            logger.warning(f"Resume {resume_id} is not yet processed (status: {resume.status}). Please wait for processing to complete.")
            return []

        if not resume.category:
            logger.warning(f"Resume {resume_id} has no category")
            return []

        category = resume.category.replace("_", " ")
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
