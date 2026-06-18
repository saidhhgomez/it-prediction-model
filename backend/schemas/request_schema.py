from pydantic import (
    BaseModel,
    Field,
    field_validator
)


class PredictionRequest(BaseModel):

    country: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    job_role: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    ai_specialization: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    experience_level: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

    experience_years: int = Field(
        ...,
        ge=0,
        le=30
    )

    education_required: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    industry: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    company_size: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    work_mode: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

    weekly_hours: float = Field(
        ...,
        ge=1,
        le=80
    )

    @field_validator(
        "country",
        "job_role",
        "ai_specialization",
        "experience_level",
        "education_required",
        "industry",
        "company_size",
        "work_mode"
    )
    @classmethod
    def validate_strings(cls, value):

        value = value.strip()

        if not value:
            raise ValueError(
                "Field cannot be empty"
            )

        return value