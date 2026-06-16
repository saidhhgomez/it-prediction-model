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

app = FastAPI()


dataset_service = DatasetService()

similarity_service = SimilarityService()

prediction_service = PredictionService()


@app.post("/predict")
def predict_future_demand(
    request: PredictionRequest
):

    df = dataset_service.get_dataset()

    similar_profiles = (
        similarity_service
        .find_similar_profiles(
            df,
            request
        )
    )

    indicators = {

        "skill_demand_score":
            similar_profiles[
                'skill_demand_score'
            ].mean(),

        "career_growth_score":
            similar_profiles[
                'career_growth_score'
            ].mean(),

        "job_openings":
            similar_profiles[
                'job_openings'
            ].mean(),

        "job_security_score":
            similar_profiles[
                'job_security_score'
            ].mean(),

        "automation_risk":
            similar_profiles[
                'automation_risk'
            ].mean(),

        "ai_adoption_score":
            similar_profiles[
                'ai_adoption_score'
            ].mean()
    }

    prediction = (
        prediction_service
        .predict(indicators)
    )

    prediction["indicators"] = {

        k: round(float(v), 2)

        for k, v in indicators.items()
    }

    return prediction