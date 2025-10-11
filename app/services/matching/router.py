from typing import List

from fastapi import APIRouter

from app.database.models import JobVacancies
from app.services.matching.methods import find_suitable_jobs

matching_router = APIRouter(prefix="/matching", tags=["matching"])


@matching_router.get("/suitable-jobs", response_model=List[JobVacancies])
async def get_suitable_jobs():
    """
    Find suitable job vacancies based on the latest uploaded resume category.
    """
    return find_suitable_jobs()
