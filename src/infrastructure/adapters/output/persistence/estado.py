from sqlalchemy import Column, Integer, String
from .base import Base


class EstadoORM(Base):
    """Modelo ORM: Estado.
    
    Catálogo genérico para estados de otras entidades (Comunicado, Archivo).
    NO se usa para Tarea (ver EstadoTarea).
    """
    __tablename__ = "estado"
    
    id_estado = Column(Integer, primary_key=True, autoincrement=True)
    nombre_estado = Column(String(100), nullable=False)
    
    def __repr__(self):
        return f"<EstadoORM(id={self.id_estado}, estado={self.nombre_estado})>"
