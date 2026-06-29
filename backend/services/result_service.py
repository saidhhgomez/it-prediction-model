from sqlalchemy.orm import Session

from backend.database.models import (
    Resultado
)


class ResultService:

    def create_result(
        self,
        db: Session,
        id_evaluacion: int,
        future_demand: dict,
        automation_risk: dict,
        career_growth: dict,
        salary_projection: dict,
        similar_profiles_found: int
    ):

        resultado = Resultado(

            id_evaluacion=id_evaluacion,

            future_demand_level=
                future_demand["prediction"],

            future_demand_confidence=
                future_demand["confidence"],

            automation_risk_level=
                automation_risk["level"],

            automation_risk_score=
                automation_risk["score"],

            career_growth_level=
                career_growth["level"],

            career_growth_score=
                career_growth["score"],

            salary_level=
                salary_projection["level"],

            average_salary_usd=
                salary_projection["average_salary_usd"],

            similar_profiles_found=
                similar_profiles_found
        )

        db.add(resultado)

        db.commit()

        db.refresh(resultado)

        return resultado