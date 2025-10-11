import json

from loguru import logger
from sqlmodel import Session

from app.celery import app
from app.database.engine import engine
from app.database.models import JobVacancies
from app.services.vacancies.methods import job_extract
from app.utils.scrapper_clients import linkedin_client


@app.task
def process_scrap():
    client = linkedin_client
    titles = [
        "Marketing",
        "Data Analyst",
        "Human Resources",
        "System Analyst",
        "Product Manager",
        "Sales Executive",
        "Recruitment Specialist",
        "Talent Acquisition",
        "Production Supervisor",
        "Maintenance Engineer",
        "Quality Assurance (QA)",
        "Quality Control (QC)",
        "Process Engineer",
        "Apoteker",
        "Designer",
        "Graphic Designer",
        "Instructional Designer",
        "UX Designer",
        "Content Creator",
        "Video Editor",
        "Compliance Officer",
        "Legal Officer",
    ]

    job_vacancies = []

    for title in titles:
        run_input = {
            "title": title,
            "location": "Indonesia",
            "rows": 30,
            "publishedAt": "r604800",
            "proxy": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"]},
        }

        logger.info(f"Processing LinkedIn jobs scraper for title: {title}")
        run = client.actor("bebity/linkedin-jobs-scraper").call(run_input=run_input)

        for item in client.dataset(run["defaultDatasetId"]).iterate_items():  # type: ignore
            try:
                raw_job_data = json.dumps(item)

                extracted_data = job_extract(raw_job_data)

                job_vacancy = JobVacancies(
                    job_id=extracted_data.get("id", ""),
                    published_at=extracted_data.get("publishedAt", ""),
                    salary=extracted_data.get("salary", ""),
                    title=extracted_data.get("title", ""),
                    job_url=extracted_data.get("jobUrl", ""),
                    company_name=extracted_data.get("companyName", ""),
                    company_url=extracted_data.get("companyUrl", ""),
                    location=extracted_data.get("location", ""),
                    posted_time=extracted_data.get("postedTime", ""),
                    applications_count=extracted_data.get("applicationsCount", ""),
                    description=extracted_data.get("description", ""),
                    contract_type=extracted_data.get("contractType", ""),
                    experience_level=extracted_data.get("experienceLevel", ""),
                    work_type=extracted_data.get("workType", ""),
                    sector=extracted_data.get("sector", ""),
                    apply_type=extracted_data.get("applyType", ""),
                    apply_url=extracted_data.get("applyUrl", ""),
                    description_html=extracted_data.get("descriptionHtml", ""),
                    company_id=extracted_data.get("companyId", ""),
                    benefits=extracted_data.get("benefits", ""),
                    poster_profile_url=extracted_data.get("posterProfileUrl", ""),
                )

                job_vacancies.append(job_vacancy)
                logger.info(f"Extracted job: {job_vacancy.title}")

            except Exception as e:
                logger.error(f"Error processing job item: {e}")
                continue

    with Session(engine) as session:
        try:
            session.add_all(job_vacancies)
            session.commit()
            logger.info(f"Successfully saved {len(job_vacancies)} jobs to database")
        except Exception as e:
            logger.error(f"Error saving jobs to database: {e}")
            session.rollback()
            raise e
