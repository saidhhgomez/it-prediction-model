from sqlalchemy.orm import Session

from backend.database.models import (
    Evaluacion
)


class EvaluationService:

    def create_evaluation(
        self,
        db: Session,
        id_usuario: int,
        request
    ):

        evaluacion = Evaluacion(

            id_usuario=id_usuario,

            country=request.country,

            job_role=request.job_role,

            ai_specialization=request.ai_specialization,

            experience_level=request.experience_level,

            experience_years=request.experience_years,

            education_required=request.education_required,

            industry=request.industry,

            company_size=request.company_size,

            work_mode=request.work_mode,

            weekly_hours=request.weekly_hours,

            idioma_ingles=request.idioma_ingles,

            github_profile=request.github_profile,

            programming_level=request.programming_level,

            certifications=request.certifications
        )

        db.add(evaluacion)

        db.commit()

        db.refresh(evaluacion)

        return evaluacion