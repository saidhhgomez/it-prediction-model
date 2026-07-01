from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import Depends

from backend.database.session import get_db

from fastapi import (
    FastAPI,
    HTTPException
)

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

from backend.services.user_service import (
    UserService
)

from backend.services.evaluation_service import (
    EvaluationService
)

from backend.services.result_service import (
    ResultService
)

from backend.services.chatgpt_service import (
    ChatGPTService
)

from backend.services.feedback_service import (
    FeedbackService
)

from backend.services.history_service import (
    HistoryService
)

app = FastAPI()


dataset_service = DatasetService()

similarity_service = SimilarityService()

prediction_service = PredictionService()

automation_service = (
    AutomationRiskService()
)

career_service = (
    CareerGrowthService()
)

salary_service = (
    SalaryProjectionService()
)

user_service = UserService()

evaluation_service = (
    EvaluationService()
)

result_service = (
    ResultService()
)

chatgpt_service = (
    ChatGPTService()
)

feedback_service = (
    FeedbackService()
)

history_service = (
    HistoryService()
)

@app.get("/test-db")
def test_db(
    db: Session = Depends(get_db)
):

    result = db.execute(
        text("SELECT NOW()")
    )

    return {
        "postgres_time":
        str(result.scalar())
    }
    
@app.get("/test-insert")
def test_insert(
    db: Session = Depends(get_db)
):

    from backend.database.models import Usuario
    import uuid

    usuario = Usuario(
        uuid_usuario=uuid.uuid4()
    )

    db.add(usuario)

    db.commit()

    db.refresh(usuario)

    return {
        "id_usuario":
        usuario.id_usuario
    }
    
from uuid import uuid4

@app.get("/test-user-service")
def test_user_service(
    db: Session = Depends(get_db)
):

    usuario = (
        user_service
        .get_or_create_user(
            db=db,
            uuid_usuario="123e4567-e89b-12d3-a456-426614174000",
            ip_registro="127.0.0.1"
        )
    )

    return {
        "id_usuario":
            usuario.id_usuario,

        "uuid_usuario":
            str(
                usuario.uuid_usuario
            )
    }
    
@app.get("/test-evaluation")
def test_evaluation(
    db: Session = Depends(get_db)
):

    class FakeRequest:

        country = "Canada"

        job_role = "Data Scientist"

        ai_specialization = "LLM"

        experience_level = "Mid"

        experience_years = 3

        education_required = "Bachelor"

        industry = "Tech"

        company_size = "Medium"

        work_mode = "Hybrid"

        weekly_hours = 40

        idioma_ingles = "Advanced"

        github_profile = True

        programming_level = "Advanced"

        certifications = True

    usuario = (
        user_service
        .get_or_create_user(
            db=db,
            uuid_usuario="123e4567-e89b-12d3-a456-426614174000"
        )
    )

    evaluacion = (
        evaluation_service
        .create_evaluation(
            db=db,
            id_usuario=usuario.id_usuario,
            request=FakeRequest()
        )
    )

    return {
        "id_evaluacion":
            evaluacion.id_evaluacion,

        "id_usuario":
            evaluacion.id_usuario
    }
    
@app.get("/test-result")
def test_result(
    db: Session = Depends(get_db)
):

    future_demand = {
        "prediction": "High",
        "confidence": 87.5
    }

    automation_risk = {
        "level": "Low",
        "score": 22.4
    }

    career_growth = {
        "level": "High",
        "score": 78.9
    }

    salary_projection = {
        "level": "Alto",
        "average_salary_usd": 125000
    }

    resultado = (
        result_service
        .create_result(
            db=db,
            id_evaluacion=1,
            future_demand=future_demand,
            automation_risk=automation_risk,
            career_growth=career_growth,
            salary_projection=salary_projection,
            similar_profiles_found=35
        )
    )

    return {
        "id_resultado":
            resultado.id_resultado,

        "id_evaluacion":
            resultado.id_evaluacion
    }
    
@app.get("/test-chatgpt")
def test_chatgpt():

    class FakeRequest:

        country = "Canada"
        job_role = "Data Scientist"
        ai_specialization = "LLM"
        experience_level = "Mid"
        experience_years = 3
        education_required = "Bachelor"
        industry = "Tech"
        company_size = "Medium"
        work_mode = "Hybrid"
        weekly_hours = 40
        idioma_ingles = "Advanced"
        github_profile = True
        programming_level = "Senior"
        certifications = True

    feedback = chatgpt_service.generate_feedback(

        request=FakeRequest(),

        future_demand={
            "prediction": "Media",
            "confidence": 99.14,
            "probabilities": {
                "Alta": 0.18,
                "Media": 99.14,
                "Baja": 0.68
            }
        },

        automation_risk={
            "level": "Medio",
            "score": 49.23
        },

        career_growth={
            "level": "Medio",
            "score": 57.42
        },

        salary_projection={
            "level": "Bajo",
            "average_salary_usd": 76039.45
        },

        market_indicators={
            "skill_demand_score": 49.67,
            "job_openings": 17.48,
            "job_security_score": 75.93,
            "ai_adoption_score": 71.72
        },

        similar_profiles_found=574

    )

    return {
        "feedback": feedback
    }
    
@app.get("/test-feedback")
def test_feedback(
    db: Session = Depends(get_db)
):

    feedback = (
        feedback_service
        .create_feedback(
            db=db,
            id_resultado=1,
            feedback="Este es un feedback de prueba."
        )
    )

    return {

        "id_feedback":
            feedback.id_feedback,

        "id_resultado":
            feedback.id_resultado
    }
    
@app.get("/test-history")
def test_history(
    db: Session = Depends(get_db)
):

    historial = (
        history_service
        .create_history(
            db=db,
            id_usuario=1,
            endpoint="/predict"
        )
    )

    return {

        "id_historial":
            historial.id_historial,

        "id_usuario":
            historial.id_usuario,

        "endpoint":
            historial.endpoint
    }

@app.post("/predict")
def predict(
    request: PredictionRequest,
    db: Session = Depends(get_db)
):

    try:

        # USUARIO

        usuario = (
            user_service
            .get_or_create_user(
                db=db,
                uuid_usuario=request.uuid_usuario
            )
        )

        # DATASET

        df = (
            dataset_service
            .get_dataset()
        )

        if df.empty:

            raise HTTPException(
                status_code=500,
                detail="Dataset is empty"
            )

        # PERFILES SIMILARES

        similar_profiles = (

            similarity_service
            .find_similar_profiles(
                df,
                request
            )
        )

        if similar_profiles.empty:

            raise HTTPException(
                status_code=404,
                detail="No similar profiles found"
            )

        # INDICADORES

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

        for key, value in indicators.items():

            if value != value:

                raise HTTPException(
                    status_code=500,
                    detail=f"Invalid indicator: {key}"
                )

        # PREDICCIONES

        future_demand = (
            prediction_service
            .predict(
                indicators
            )
        )

        automation_risk = (
            automation_service
            .predict(
                similar_profiles
            )
        )

        career_growth = (
            career_service
            .predict(
                similar_profiles
            )
        )

        salary_projection = (
            salary_service
            .predict(
                similar_profiles
            )
        )

        # GUARDAR EVALUACION

        evaluacion = (
            evaluation_service
            .create_evaluation(
                db=db,
                id_usuario=usuario.id_usuario,
                request=request
            )
        )

        # GUARDAR RESULTADO

        result_service.create_result(
            db=db,
            id_evaluacion=evaluacion.id_evaluacion,
            future_demand=future_demand,
            automation_risk=automation_risk,
            career_growth=career_growth,
            salary_projection=salary_projection,
            similar_profiles_found=len(similar_profiles)
        )

        # RESPONSE

        return {

            "input_profile": request.model_dump(),

            "future_demand": {

                "level":
                    future_demand[
                        "prediction"
                    ],

                "confidence":
                    future_demand[
                        "confidence"
                    ],

                "probabilities":
                    future_demand[
                        "probabilities"
                    ]
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
                len(
                    similar_profiles
                )
        }

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )