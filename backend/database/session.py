from sqlalchemy.orm import sessionmaker

from backend.database.connection import engine

# SESSION FACTORY

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# DEPENDENCY FASTAPI

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()