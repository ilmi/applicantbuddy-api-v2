from enum import Enum
from typing import List, Optional

from sqlmodel import JSON, Column, Field

from app.core.models import BaseModel
from app.utils.generate_ids import generate_id


class User(BaseModel, table=True):
    id: str = Field(default_factory=generate_id, primary_key=True)
    email: str = Field(unique=True, index=True)
    password_hash: str
    username: str = Field(unique=True, index=True)
    is_active: bool = Field(default=True)
    role: str = Field(default="user")


class ResumeStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"


class Resume(BaseModel, table=True):
    fullname: Optional[str] = Field("")
    email: Optional[str] = Field("")
    phone: Optional[str] = Field("")
    address: Optional[str] = Field("")
    category: Optional[str] = Field("")
    summary: Optional[str] = Field("")
    raw_resume: Optional[str] = Field("")
    file_name: Optional[str] = Field("")
    file_path: Optional[str] = Field("")
    status: ResumeStatus = Field(default=ResumeStatus.PENDING)
    skills: Optional[List[str]] = Field(default_factory=list, sa_column=Column(JSON))
    strength: Optional[List[str]] = Field(default_factory=list, sa_column=Column(JSON))


class JobVacancies(BaseModel, table=True):
    job_id: Optional[str] = None
    published_at: Optional[str] = Field(default="")
    salary: Optional[str] = Field(default="")
    title: Optional[str] = Field(default="")
    job_url: Optional[str] = Field(default="")
    company_name: Optional[str] = Field(default="")
    company_url: Optional[str] = Field(default="")
    location: Optional[str] = Field(default="")
    posted_time: Optional[str] = Field(default="")
    applications_count: Optional[str] = Field(default="")
    description: Optional[str] = Field(default="")
    contract_type: Optional[str] = Field(default="")
    experience_level: Optional[str] = Field(default="")
    work_type: Optional[str] = Field(default="")
    sector: Optional[str] = Field(default="")
    apply_type: Optional[str] = Field(default="")
    apply_url: Optional[str] = Field(default="")
    description_html: Optional[str] = Field(default="")
    company_id: Optional[str] = Field(default="")
    benefits: Optional[str] = Field(default="")
    poster_profile_url: Optional[str] = Field(default="")
