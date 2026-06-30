from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from src.infrastructure.config.database import Base


class CatalogoModel(Base):
    __tablename__ = "catalogos"
    
    id_catalogo = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_catalogo = Column(String(100), nullable=False)
    id_tipo_catalogo = Column(Integer, ForeignKey("tipos_catalogo.id_tipo_catalogo"), nullable=False)
    descripcion = Column(String(255))
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    activo = Column(Integer, default=1)