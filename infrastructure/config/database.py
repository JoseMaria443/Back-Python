"""Configuración de base de datos con SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# URL de conexión a PostgreSQL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://usuario:password@localhost:5432/nombre_db"
)

# Crear engine de SQLAlchemy
engine = create_engine(DATABASE_URL)

# SessionLocal para obtener sesiones de BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()


def get_db():
    """Dependency para obtener sesión de base de datos.
    
    Yields:
        Session: Sesión de SQLAlchemy
    
    Example:
        @app.get("/endpoint")
        def endpoint(db: Session = Depends(get_db)):
            # usar db aquí
            pass
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Inicializa las tablas en la base de datos.
    
    Crea todas las tablas definidas en los modelos que hereden de Base.
    """
    Base.metadata.create_all(bind=engine)


def drop_all_tables():
    """Elimina todas las tablas de la base de datos.
    
    ⚠️ CUIDADO: Esta función elimina TODOS los datos.
    Solo usar en desarrollo o testing.
    """
    Base.metadata.drop_all(bind=engine)