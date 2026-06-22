from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TareaORM(Base):
    """Modelo ORM: Tarea.
    
    Mapeo a tabla PostgreSQL 'tarea' con relación a EstadoTarea.
    """
    __tablename__ = "tarea"
    
    id_tarea = Column(Integer, primary_key=True, autoincrement=True)
    id_comunicado = Column(Integer, nullable=False)
    descripcion = Column(Text, nullable=False)
    fecha_entrega = Column(Date, nullable=False)
    fecha_registro = Column(Date, nullable=False)
    id_estado_tarea = Column(Integer, nullable=True)  # FK -> estado_tarea.id_estado_tarea
    
    def __repr__(self):
        return f"<TareaORM(id={self.id_tarea}, comunicado={self.id_comunicado})>"
