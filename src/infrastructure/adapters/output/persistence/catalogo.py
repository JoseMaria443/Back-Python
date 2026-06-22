from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base


class CatalogoORM(Base):
    """Modelo ORM: Catalogo.
    
    Catálogo genérico para valores comunes (TipoComunicado, MetodoRecepcion, etc).
    """
    __tablename__ = "catalogo"
    
    id_catalogo = Column(Integer, primary_key=True, autoincrement=True)
    id_tipo_catalogo = Column(Integer, ForeignKey("tipo_catalogo.id_tipo_catalogo"), nullable=False)
    descripcion = Column(String(255), nullable=False)
    
    def __repr__(self):
        return f"<CatalogoORM(id={self.id_catalogo}, tipo={self.id_tipo_catalogo}, desc={self.descripcion})>"