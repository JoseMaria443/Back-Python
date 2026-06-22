import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password@localhost:5432/comunicados_db"
)

# Crear engine de SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    echo=os.getenv("SQL_ECHO", "False").lower() == "true",
    future=True
)

# Session factory
SessionLocal = sessionmaker(
    bind=engine,
    class_=Session,
    expire_on_commit=False
)


def get_db() -> Session:
    """Dependency injection para obtener sesión de BD en FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
