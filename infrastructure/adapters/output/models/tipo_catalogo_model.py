from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.infrastructure.config.database import Base


class TipoCatalogoModel(Base):
    __tablename__ = "tipos_catalogo"
    
    id_tipo_catalogo = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_tipo_catalogo = Column(String(100), unique=True, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)