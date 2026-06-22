from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class TareaResponsableORM(Base):
    """Modelo ORM: TareaResponsable.
    
    Asociativa entre Tarea y Empleado (responsable) con rol.
    """
    __tablename__ = "tarea_responsable"
    
    id_tarea = Column(Integer, ForeignKey("tarea.id_tarea"), primary_key=True)
    id_responsable = Column(Integer, ForeignKey("empleado.id_empleado"), primary_key=True)
    id_rol = Column(Integer, ForeignKey("rol_responsable.id_rol"), nullable=False)
    
    def __repr__(self):
        return f"<TareaResponsableORM(tarea={self.id_tarea}, resp={self.id_responsable}, rol={self.id_rol})>"
