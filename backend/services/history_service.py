from sqlalchemy.orm import Session

from backend.database.models import (
    HistorialConsulta
)


class HistoryService:

    def create_history(
        self,
        db: Session,
        id_usuario: int,
        endpoint: str
    ):

        historial = (
            HistorialConsulta(

                id_usuario=
                    id_usuario,

                endpoint=
                    endpoint
            )
        )

        db.add(
            historial
        )

        db.commit()

        db.refresh(
            historial
        )

        return historial