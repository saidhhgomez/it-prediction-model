from pydantic import BaseModel


class PredictionRequest(BaseModel):

    country: str

    job_role: str

    ai_specialization: str

    experience_level: str

    experience_years: int

    education_required: str

    industry: str

    company_size: str

    work_mode: str

    weekly_hours: float