from sqlalchemy.orm import Session

from backend.database.models import (
    HistorialConsulta,
    Usuario,
    Evaluacion,
    Resultado,
    FeedbackChatGPT
)


class HistoryService:

    # GUARDAR HISTORIAL

    def create_history(
        self,
        db: Session,
        id_usuario: int,
        endpoint: str
    ):

        historial = HistorialConsulta(
            id_usuario=id_usuario,
            endpoint=endpoint
        )

        db.add(historial)
        db.commit()
        db.refresh(historial)

        return historial

    # OBTENER HISTORIAL POR UUID

    def get_history_by_uuid(
        self,
        db: Session,
        uuid_usuario: str
    ):

        results = (

            db.query(
                Usuario,
                Evaluacion,
                Resultado
            )

            .join(
                Evaluacion,
                Usuario.id_usuario == Evaluacion.id_usuario
            )

            .join(
                Resultado,
                Evaluacion.id_evaluacion == Resultado.id_evaluacion
            )

            .filter(
                Usuario.uuid_usuario == uuid_usuario
            )

            .order_by(
                Resultado.fecha_resultado.desc()
            )

            .all()

        )

        if not results:
            return None

        history = []

        for usuario, evaluacion, resultado in results:

            history.append({

                "id_resultado": resultado.id_resultado,

                "evaluation_date": resultado.fecha_resultado,

                "profile": {

                    "country": evaluacion.country,

                    "job_role": evaluacion.job_role,

                    "ai_specialization": evaluacion.ai_specialization,

                    "experience_level": evaluacion.experience_level

                },

                "summary": {

                    "future_demand": resultado.future_demand_level,

                    "career_growth": resultado.career_growth_level,

                    "automation_risk": resultado.automation_risk_level,

                    "salary_level": resultado.salary_level

                }

            })

        return {

            "uuid_usuario": str(uuid_usuario),

            "total_evaluations": len(history),

            "evaluations": history

        }
    
    def get_result_by_id(
        self,
        db: Session,
        id_resultado: int
    ):

        result = (

            db.query(
                Usuario,
                Evaluacion,
                Resultado,
                FeedbackChatGPT
            )

            .join(
                Evaluacion,
                Usuario.id_usuario == Evaluacion.id_usuario
            )

            .join(
                Resultado,
                Evaluacion.id_evaluacion == Resultado.id_evaluacion
            )

            .outerjoin(
                FeedbackChatGPT,
                Resultado.id_resultado == FeedbackChatGPT.id_resultado
            )

            .filter(
                Resultado.id_resultado == id_resultado
            )

            .first()
        )

        if result is None:
            return None

        usuario, evaluacion, resultado, feedback = result

        nombre_usuario = "Usuario"

        if (
            feedback
            and feedback.feedback
            and isinstance(feedback.feedback, dict)
        ):

            title = feedback.feedback.get("title")

            if title and " para " in title:

                try:

                    nombre_usuario = (
                        title
                        .split(" para ")[1]
                        .split(":")[0]
                        .strip()
                    )

                except Exception:
                    pass

        return {

            "input_profile": {

                "uuid_usuario":
                    str(usuario.uuid_usuario),

                "country":
                    evaluacion.country,

                "job_role":
                    evaluacion.job_role,

                "ai_specialization":
                    evaluacion.ai_specialization,

                "experience_level":
                    evaluacion.experience_level,

                "experience_years":
                    evaluacion.experience_years,

                "education_required":
                    evaluacion.education_required,

                "industry":
                    evaluacion.industry,

                "company_size":
                    evaluacion.company_size,

                "work_mode":
                    evaluacion.work_mode,

                "weekly_hours":
                    float(evaluacion.weekly_hours),

                "idioma_ingles":
                    evaluacion.idioma_ingles,

                "github_profile":
                    evaluacion.github_profile,

                "programming_level":
                    evaluacion.programming_level,

                "certifications":
                    evaluacion.certifications,

                "nombre_usuario":
                    nombre_usuario
            },

            "future_demand": {

                "level":
                    resultado.future_demand_level,

                "confidence":
                    float(resultado.future_demand_confidence),

                "probabilities":
                    resultado.future_demand_probabilities
            },

            "automation_risk": {

                "level":
                    resultado.automation_risk_level,

                "score":
                    float(resultado.automation_risk_score)
            },

            "career_growth": {

                "level":
                    resultado.career_growth_level,

                "score":
                    float(resultado.career_growth_score)
            },

            "salary_projection": {

                "level":
                    resultado.salary_level,

                "average_salary_usd":
                    float(resultado.average_salary_usd)
            },

            "market_indicators": {

                "skill_demand_score":
                    float(resultado.skill_demand_score),

                "job_openings":
                    float(resultado.job_openings),

                "job_security_score":
                    float(resultado.job_security_score),

                "ai_adoption_score":
                    float(resultado.ai_adoption_score)
            },

            "model_information": {

                "accuracy": 98.21,

                "precision": 98.21,

                "recall": 98.21,

                "f1_score": 98.20,

                "dataset":
                    "Global AI and Data Jobs Salary Dataset"
            },

            "similar_profiles_found":
                resultado.similar_profiles_found,

            "feedback":
                feedback.feedback if feedback else None
        }