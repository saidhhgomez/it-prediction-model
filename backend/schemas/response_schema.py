from pydantic import BaseModel

from typing import Dict


class FutureDemandResponse(BaseModel):

    level: str

    confidence: float

    probabilities: Dict[str, float]


class AutomationRiskResponse(BaseModel):

    level: str

    score: float


class CareerGrowthResponse(BaseModel):

    level: str

    score: float


class SalaryProjectionResponse(BaseModel):

    level: str

    average_salary_usd: float


class MarketIndicatorsResponse(BaseModel):

    skill_demand_score: float

    job_openings: float

    job_security_score: float

    ai_adoption_score: float


class PredictionResponse(BaseModel):

    input_profile: dict

    future_demand: FutureDemandResponse

    automation_risk: AutomationRiskResponse

    career_growth: CareerGrowthResponse

    salary_projection: SalaryProjectionResponse

    market_indicators: MarketIndicatorsResponse

    similar_profiles_found: int