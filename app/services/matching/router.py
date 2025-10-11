from typing import List

from fastapi import APIRouter

from app.database.models import JobVacancies
from app.services.matching.methods import find_suitable_jobs

matching_router = APIRouter(prefix="/matching", tags=["matching"])


@matching_router.get("/suitable-jobs/{resume_id}", response_model=List[JobVacancies])
async def get_suitable_jobs(resume_id: str):
    """
    Find suitable job vacancies based on the specified resume category.
    The resume must be fully processed (status: completed) before job matching can occur.
    """
    return find_suitable_jobs(resume_id)
