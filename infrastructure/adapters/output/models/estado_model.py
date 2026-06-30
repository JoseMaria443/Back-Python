from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.infrastructure.config.database import Base


class EstadoModel(Base):
    __tablename__ = "estados"
    
    id_estado = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_estado = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(255))
    fecha_creacion = Column(DateTime, default=datetime.utcnow)