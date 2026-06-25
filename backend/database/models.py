from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    Text,
    ForeignKey,
    DateTime,
    Boolean
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from backend.database.connection import Base


class Usuario(Base):

    __tablename__ = "usuario"

    id_usuario = Column(
        Integer,
        primary_key=True,
        index=True
    )

    uuid_usuario = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False
    )

    ip_registro = Column(
        String(100)
    )

    fecha_registro = Column(
        DateTime,
        server_default=func.now()
    )

    evaluaciones = relationship(
        "Evaluacion",
        back_populates="usuario"
    )

    historial = relationship(
        "HistorialConsulta",
        back_populates="usuario"
    )


class Evaluacion(Base):

    __tablename__ = "evaluacion"

    id_evaluacion = Column(
        Integer,
        primary_key=True,
        index=True
    )

    id_usuario = Column(
        Integer,
        ForeignKey(
            "usuario.id_usuario"
        ),
        nullable=False
    )

    country = Column(String(100))
    job_role = Column(String(100))
    ai_specialization = Column(String(100))
    experience_level = Column(String(50))
    experience_years = Column(Integer)
    education_required = Column(String(100))
    industry = Column(String(100))
    company_size = Column(String(50))
    work_mode = Column(String(50))
    weekly_hours = Column(
        Numeric(10, 2)
    )
    
    idioma_ingles = Column(String(20))

    github_profile = Column(Boolean)

    programming_level = Column(String(20))

    certifications = Column(Boolean)

    fecha_evaluacion = Column(
        DateTime,
        server_default=func.now()
    )

    usuario = relationship(
        "Usuario",
        back_populates="evaluaciones"
    )

    resultado = relationship(
        "Resultado",
        uselist=False,
        back_populates="evaluacion"
    )


class Resultado(Base):

    __tablename__ = "resultado"

    id_resultado = Column(
        Integer,
        primary_key=True,
        index=True
    )

    id_evaluacion = Column(
        Integer,
        ForeignKey(
            "evaluacion.id_evaluacion"
        ),
        nullable=False
    )

    future_demand_level = Column(
        String(20)
    )

    future_demand_confidence = Column(
        Numeric(10, 2)
    )

    automation_risk_level = Column(
        String(20)
    )

    automation_risk_score = Column(
        Numeric(10, 2)
    )

    career_growth_level = Column(
        String(20)
    )

    career_growth_score = Column(
        Numeric(10, 2)
    )

    salary_level = Column(
        String(20)
    )

    average_salary_usd = Column(
        Numeric(12, 2)
    )

    similar_profiles_found = Column(
        Integer
    )

    fecha_resultado = Column(
        DateTime,
        server_default=func.now()
    )

    evaluacion = relationship(
        "Evaluacion",
        back_populates="resultado"
    )

    feedback = relationship(
        "FeedbackChatGPT",
        back_populates="resultado"
    )


class FeedbackChatGPT(Base):

    __tablename__ = "feedback_chatgpt"

    id_feedback = Column(
        Integer,
        primary_key=True,
        index=True
    )

    id_resultado = Column(
        Integer,
        ForeignKey(
            "resultado.id_resultado"
        ),
        nullable=False
    )

    feedback = Column(Text)

    fecha_generacion = Column(
        DateTime,
        server_default=func.now()
    )

    resultado = relationship(
        "Resultado",
        back_populates="feedback"
    )


class HistorialConsulta(Base):

    __tablename__ = "historial_consulta"

    id_historial = Column(
        Integer,
        primary_key=True,
        index=True
    )

    id_usuario = Column(
        Integer,
        ForeignKey(
            "usuario.id_usuario"
        ),
        nullable=False
    )

    endpoint = Column(
        String(100)
    )

    fecha_consulta = Column(
        DateTime,
        server_default=func.now()
    )

    usuario = relationship(
        "Usuario",
        back_populates="historial"
    )