from pydantic import BaseModel, Field


class ExtractVacancies(BaseModel):
    id: str = Field(description="Unique identifier of the job post", default="")
    publishedAt: str = Field(description="Publication date of the job post in YYYY-MM-DD format", default="")
    salary: str = Field(description="Salary information provided in the job listing, if available", default="")
    title: str = Field(description="Title of the job position", default="")
    jobUrl: str = Field(description="URL to the full job posting", default="")
    companyName: str = Field(description="Name of the company offering the job", default="")
    companyUrl: str = Field(description="URL of the company’s profile or website", default="")
    location: str = Field(description="Job location (city, region, country)", default="")
    postedTime: str = Field(description="Relative time since the job was posted (e.g., '23 hours ago')", default="")
    applicationsCount: str = Field(description="Number of applicants or application count text", default="")
    description: str = Field(description="Plain text version of the job description", default="")
    contractType: str = Field(
        description="Type of employment contract (e.g., Full-time, Part-time, Internship)", default=""
    )
    experienceLevel: str = Field(description="Required experience level (e.g., Entry level, Mid-senior)", default="")
    workType: str = Field(description="Type of work or job category (e.g., Engineering, Marketing)", default="")
    sector: str = Field(description="Industry or business sector of the company", default="")
    applyType: str = Field(description="Type of application process (e.g., EASY_APPLY, EXTERNAL_APPLY)", default="")
    applyUrl: str = Field(description="Direct link to the application form or submission page", default="")
    descriptionHtml: str = Field(description="HTML formatted version of the job description", default="")
    companyId: str = Field(description="Unique company identifier on the platform", default="")
    benefits: str = Field(description="List of benefits or perks offered for the job, if available", default="")
    posterProfileUrl: str = Field(description="Profile URL of the person or recruiter who posted the job", default="")
