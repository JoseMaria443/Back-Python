from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ComunicadoAdjuntoORM(Base):
    """Modelo ORM: Comunicado_Adjunto.
    
    Asociativa entre Comunicado y Archivo.
    Un Comunicado puede tener varios archivos adjuntos.
    """
    __tablename__ = "comunicado_adjunto"
    
    id_comunicado = Column(Integer, ForeignKey("comunicado.id_comunicado"), primary_key=True)
    id_archivo = Column(Integer, ForeignKey("archivo.id_archivo"), primary_key=True)
    
    def __repr__(self):
        return f"<ComunicadoAdjuntoORM(comunicado={self.id_comunicado}, archivo={self.id_archivo})>"
