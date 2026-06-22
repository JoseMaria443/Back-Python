from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class EstadoTareaORM(Base):
    """Modelo ORM: EstadoTarea.
    
    Catálogo específico para estados de tareas.
    """
    __tablename__ = "estado_tarea"
    
    id_estado_tarea = Column(Integer, primary_key=True, autoincrement=True)
    nombre_estado = Column(String(100), nullable=False)
    
    def __repr__(self):
        return f"<EstadoTareaORM(id={self.id_estado_tarea}, estado={self.nombre_estado})>"
