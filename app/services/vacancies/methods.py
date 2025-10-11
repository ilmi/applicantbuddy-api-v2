from app.services.vacancies.schema import ExtractVacancies
from app.utils.llm_clients import openai_client


def job_extract(job_description: str) -> dict:
    SYSTEM_PROMPT = """
        You are a job posting data extractor.
        Your task is to extract structured information from a job description or job listing text.
        You must identify key attributes such as job title, company details, job type, and description content.

        Extract the following information according to the schema below:
        - id: Unique identifier of the job post (if not available, leave empty)
        - publishedAt: Date when the job was published (YYYY-MM-DD format)
        - salary: Salary information provided in the listing
        - title: Job title exactly as mentioned
        - jobUrl: URL of the job posting
        - companyName: Name of the company offering the job
        - companyUrl: Company profile URL or website
        - location: Job location (city, region, country)
        - postedTime: Relative time since posting (e.g., "2 days ago")
        - applicationsCount: Number of applicants (e.g., "38 applicants")
        - description: Plain text job description (summarized if very long)
        - contractType: Employment type (Full-time, Part-time, Contract, Internship, etc.)
        - experienceLevel: Required experience level (Entry level, Mid-Senior, etc.)
        - workType: General job category (e.g., Engineering and Information Technology)
        - sector: Industry or business sector
        - applyType: Application method (EASY_APPLY, EXTERNAL_APPLY, etc.)
        - applyUrl: Direct application link
        - descriptionHtml: HTML-formatted job description (if available)
        - companyId: Unique company identifier (if available)
        - benefits: List or summary of job benefits/perks
        - posterProfileUrl: Recruiter or job poster's profile link

        Guidelines:
        - Extract all values directly from the text or structured job data if possible.
        - Summarize long text (like description) to concise, clear sentences.
        - If information is not available, set empty string ("") for text fields.
        - Do not invent or infer data that is not explicitly or clearly implied.
        - Maintain clean, human-readable formatting in extracted text.
        - Ensure all fields conform exactly to the JobPosting schema.
    """

    try:
        response = openai_client.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Job description: {job_description}"},
            ],
            response_format=ExtractVacancies,
        )

        if response.choices[0].message.parsed:
            job_data = response.choices[0].message.parsed
            return job_data.model_dump()
        else:
            # Fallback if parsing fails
            return {
                "id": "",
                "publishedAt": "",
                "salary": "",
                "title": "",
                "jobUrl": "",
                "companyName": "",
                "companyUrl": "",
                "location": "",
                "postedTime": "",
                "applicationsCount": "",
                "description": "",
                "contractType": "",
                "experienceLevel": "",
                "workType": "",
                "sector": "",
                "applyType": "",
                "applyUrl": "",
                "descriptionHtml": "",
                "companyId": "",
                "benefits": "",
                "posterProfileUrl": "",
            }
    except Exception as e:
        # Log the error and return default values
        print(f"Error extracting job information: {e}")
        return {
            "id": "",
            "publishedAt": "",
            "salary": "",
            "title": "",
            "jobUrl": "",
            "companyName": "",
            "companyUrl": "",
            "location": "",
            "postedTime": "",
            "applicationsCount": "",
            "description": "",
            "contractType": "",
            "experienceLevel": "",
            "workType": "",
            "sector": "",
            "applyType": "",
            "applyUrl": "",
            "descriptionHtml": "",
            "companyId": "",
            "benefits": "",
            "posterProfileUrl": "",
        }
