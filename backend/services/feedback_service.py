from sqlalchemy.orm import Session

from backend.database.models import (
    FeedbackChatGPT
)


class FeedbackService:

    def create_feedback(
        self,
        db: Session,
        id_resultado: int,
        feedback: dict
    ):

        nuevo_feedback = FeedbackChatGPT(

            id_resultado=id_resultado,

            feedback=feedback
        )

        db.add(
            nuevo_feedback
        )

        db.commit()

        db.refresh(
            nuevo_feedback
        )

        return nuevo_feedback