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
                Resultado,
                FeedbackChatGPT
            )

            .join(Evaluacion, Usuario.id_usuario == Evaluacion.id_usuario)
            .join(Resultado, Evaluacion.id_evaluacion == Resultado.id_evaluacion)
            .outerjoin(FeedbackChatGPT, Resultado.id_resultado == FeedbackChatGPT.id_resultado)

            .filter(Usuario.uuid_usuario == uuid_usuario)

            .order_by(Resultado.fecha_resultado.desc())

            .all()
        )

        if not results:
            return None

        history = []

        for usuario, evaluacion, resultado, feedback in results:

            history.append({

                "evaluation_date": resultado.fecha_resultado,

                "profile": {
                    "country": evaluacion.country,
                    "job_role": evaluacion.job_role,
                    "ai_specialization": evaluacion.ai_specialization,
                    "experience_level": evaluacion.experience_level,
                    "experience_years": evaluacion.experience_years,
                    "education_required": evaluacion.education_required,
                    "industry": evaluacion.industry,
                    "company_size": evaluacion.company_size,
                    "work_mode": evaluacion.work_mode
                },

                "results": {

                    "future_demand": {
                        "level": resultado.future_demand_level,
                        "confidence": float(resultado.future_demand_confidence)
                    },

                    "automation_risk": {
                        "level": resultado.automation_risk_level,
                        "score": float(resultado.automation_risk_score)
                    },

                    "career_growth": {
                        "level": resultado.career_growth_level,
                        "score": float(resultado.career_growth_score)
                    },

                    "salary": {
                        "level": resultado.salary_level,
                        "average_salary_usd": float(resultado.average_salary_usd)
                    },

                    "similar_profiles_found": resultado.similar_profiles_found
                },

                "feedback": feedback.feedback if feedback else None
            })

        return {
            "uuid_usuario": str(uuid_usuario),
            "total_evaluations": len(history),
            "evaluations": history
        }