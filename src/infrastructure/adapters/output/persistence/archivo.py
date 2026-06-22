from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from .base import Base


class ArchivoORM(Base):
    """Modelo ORM: Archivo.
    
    Mapeo a tabla PostgreSQL 'archivo'.
    Un archivo puede ser adjunto de un Comunicado o de una Tarea.
    """
    __tablename__ = "archivo"
    
    id_archivo = Column(Integer, primary_key=True, autoincrement=True)
    doi = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=False)
    url_archivo = Column(String(500), nullable=False)
    nombre_original = Column(String(255), nullable=False)
    id_elaborador = Column(Integer, ForeignKey("empleado.id_empleado"), nullable=False)
    fecha_registro = Column(Date, nullable=False)
    
    def __repr__(self):
        return f"<ArchivoORM(id={self.id_archivo}, nombre={self.nombre_original})>"
