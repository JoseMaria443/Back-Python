from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class TareaArchivoORM(Base):
    """Modelo ORM: TareaArchivo.
    
    Asociativa entre Tarea y Archivo.
    """
    __tablename__ = "tarea_archivo"
    
    id_tarea = Column(Integer, ForeignKey("tarea.id_tarea"), primary_key=True)
    id_archivo = Column(Integer, ForeignKey("archivo.id_archivo"), primary_key=True)
    
    def __repr__(self):
        return f"<TareaArchivoORM(tarea={self.id_tarea}, archivo={self.id_archivo})>"
