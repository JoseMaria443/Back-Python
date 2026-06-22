from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class ComunicadoDestinatarioORM(Base):
    """Modelo ORM: ComunicadoDestinatario.
    
    Asociativa entre Comunicado y Destinatario con rol específico.
    """
    __tablename__ = "comunicado_destinatario"
    
    id_comunicado = Column(Integer, ForeignKey("comunicado.id_comunicado"), primary_key=True)
    id_destinatario = Column(Integer, primary_key=True)
    id_rol_destinatario = Column(Integer, ForeignKey("rol_destinatario.id_rol"), nullable=False)
    
    def __repr__(self):
        return f"<ComunicadoDestinatarioORM(com={self.id_comunicado}, dest={self.id_destinatario}, rol={self.id_rol_destinatario})>"
