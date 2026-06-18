from fastapi import FastAPI

from backend.schemas.request_schema import (
    PredictionRequest
)

from backend.services.dataset_service import (
    DatasetService
)

from backend.services.similarity_service import (
    SimilarityService
)

from backend.services.prediction_service import (
    PredictionService
)

from backend.services.automation_risk_service import (
    AutomationRiskService
)

from backend.services.career_growth_service import (
    CareerGrowthService
)

from backend.services.salary_projection_service import (
    SalaryProjectionService
)

app = FastAPI()

dataset_service = DatasetService()

similarity_service = SimilarityService()

prediction_service = PredictionService()

automation_service = AutomationRiskService()

career_service = CareerGrowthService()

salary_service = SalaryProjectionService()


@app.post("/predict")
def predict(request: PredictionRequest):

    # DATASET

    df = dataset_service.get_dataset()

    # PERFILES SIMILARES

    similar_profiles = (
        similarity_service.find_similar_profiles(
            df,
            request
        )
    )

    # INDICADORES PROMEDIO

    indicators = {

        "skill_demand_score":
            similar_profiles[
                "skill_demand_score"
            ].mean(),

        "career_growth_score":
            similar_profiles[
                "career_growth_score"
            ].mean(),

        "job_openings":
            similar_profiles[
                "job_openings"
            ].mean(),

        "job_security_score":
            similar_profiles[
                "job_security_score"
            ].mean(),

        "automation_risk":
            similar_profiles[
                "automation_risk"
            ].mean(),

        "ai_adoption_score":
            similar_profiles[
                "ai_adoption_score"
            ].mean()
    }

    # MODELO DEMANDA FUTURA

    future_demand = (
        prediction_service.predict(
            indicators
        )
    )
    
    # SERVICIOS ADICIONALES

    automation_risk = (
        automation_service.predict(
            similar_profiles
        )
    )

    career_growth = (
        career_service.predict(
            similar_profiles
        )
    )

    salary_projection = (
        salary_service.predict(
            similar_profiles
        )
    )

    # RESPONSE

    return {

        "input_profile": {

            "country":
                request.country,

            "job_role":
                request.job_role,

            "ai_specialization":
                request.ai_specialization,

            "experience_level":
                request.experience_level,

            "experience_years":
                request.experience_years,

            "education_required":
                request.education_required,

            "industry":
                request.industry,

            "company_size":
                request.company_size,

            "work_mode":
                request.work_mode,

            "weekly_hours":
                request.weekly_hours
        },

        "future_demand": {

            "level":
                future_demand["prediction"],

            "confidence":
                future_demand["confidence"],

            "probabilities":
                future_demand["probabilities"]
        },

        "automation_risk":
            automation_risk,

        "career_growth":
            career_growth,

        "salary_projection":
            salary_projection,

        "market_indicators": {

            "skill_demand_score":
                round(
                    float(
                        indicators[
                            "skill_demand_score"
                        ]
                    ),
                    2
                ),

            "job_openings":
                round(
                    float(
                        indicators[
                            "job_openings"
                        ]
                    ),
                    2
                ),

            "job_security_score":
                round(
                    float(
                        indicators[
                            "job_security_score"
                        ]
                    ),
                    2
                ),

            "ai_adoption_score":
                round(
                    float(
                        indicators[
                            "ai_adoption_score"
                        ]
                    ),
                    2
                )
        },

        "similar_profiles_found":
            len(similar_profiles)
    }