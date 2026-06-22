from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from .base import Base


class ComunicadoORM(Base):
    """Modelo ORM: Comunicado.
    
    Mapeo a tabla PostgreSQL 'comunicado' sin campo IdArchivo directo.
    Archivos adjuntos vía Comunicado_adjunto.
    """
    __tablename__ = "comunicado"
    
    id_comunicado = Column(Integer, primary_key=True, autoincrement=True)
    doi = Column(String(255), nullable=False)
    num_comunicado = Column(String(255), nullable=False)
    id_emisor = Column(Integer, nullable=False)
    fecha_recepcion = Column(Date, nullable=False)
    id_destinatario = Column(Integer, nullable=False)
    fecha_registro = Column(Date, nullable=False)
    id_registro = Column(Integer, nullable=False)
    id_metodo_recepcion = Column(Integer, nullable=False)
    tema = Column(String(255), nullable=False)
    observaciones = Column(Text, nullable=True)
    id_tipo_comunicado = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"<ComunicadoORM(id={self.id_comunicado}, num={self.num_comunicado})>"
