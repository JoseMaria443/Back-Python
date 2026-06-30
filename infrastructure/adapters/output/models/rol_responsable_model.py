from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.infrastructure.config.database import Base


class RolResponsableModel(Base):
    __tablename__ = "roles_responsable"
    
    id_rol_responsable = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_rol = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(255))
    fecha_creacion = Column(DateTime, default=datetime.utcnow)