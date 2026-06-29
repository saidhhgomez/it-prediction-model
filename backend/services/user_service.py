from uuid import UUID

from sqlalchemy.orm import Session

from backend.database.models import Usuario


class UserService:

    def get_by_uuid(
        self,
        db: Session,
        uuid_usuario: str
    ):

        return (
            db.query(Usuario)
            .filter(
                Usuario.uuid_usuario ==
                UUID(uuid_usuario)
            )
            .first()
        )

    def create_user(
        self,
        db: Session,
        uuid_usuario: str,
        ip_registro: str = None
    ):

        usuario = Usuario(

            uuid_usuario=UUID(
                uuid_usuario
            ),

            ip_registro=ip_registro
        )

        db.add(usuario)

        db.commit()

        db.refresh(usuario)

        return usuario

    def get_or_create_user(
        self,
        db: Session,
        uuid_usuario: str,
        ip_registro: str = None
    ):

        usuario = self.get_by_uuid(
            db,
            uuid_usuario
        )

        if usuario:
            return usuario

        return self.create_user(
            db,
            uuid_usuario,
            ip_registro
        )