from datetime import datetime, timedelta

from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.database.models import (
    Evaluacion,
    Resultado
)


class ValidationService:

    HOURS_LIMIT = 12

    def validate_prediction_limit(
        self,
        db: Session,
        id_usuario: int
    ):

        ultimo_resultado = (

            db.query(Resultado)

            .join(
                Evaluacion,
                Resultado.id_evaluacion == Evaluacion.id_evaluacion
            )

            .filter(
                Evaluacion.id_usuario == id_usuario
            )

            .order_by(
                Resultado.fecha_resultado.desc()
            )

            .first()

        )

        # Nunca ha realizado una evaluación

        if ultimo_resultado is None:

            return

        ahora = datetime.now()

        fecha_ultimo_resultado = (
            ultimo_resultado.fecha_resultado
        )

        tiempo_transcurrido = (
            ahora - fecha_ultimo_resultado
        )

        if tiempo_transcurrido >= timedelta(
            hours=self.HOURS_LIMIT
        ):

            return

        tiempo_restante = (
            timedelta(hours=self.HOURS_LIMIT)
            - tiempo_transcurrido
        )

        horas_restantes = round(
            tiempo_restante.total_seconds() / 3600,
            2
        )

        raise HTTPException(

            status_code=429,

            detail={

                "success": False,

                "message": (
                    "Ya realizaste una evaluación recientemente. "
                    "Debes esperar antes de generar una nueva predicción."
                ),

                "remaining_hours":
                    horas_restantes,

                "next_evaluation":
                    (
                        fecha_ultimo_resultado
                        + timedelta(
                            hours=self.HOURS_LIMIT
                        )
                    ).isoformat()

            }

        )