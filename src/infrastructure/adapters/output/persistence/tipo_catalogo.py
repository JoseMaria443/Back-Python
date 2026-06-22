from sqlalchemy import Column, Integer, String
from .base import Base


class TipoCatalogoORM(Base):
    """Modelo ORM: TipoCatalogo.
    
    Define los tipos de catálogos disponibles.
    """
    __tablename__ = "tipo_catalogo"
    
    id_tipo_catalogo = Column(Integer, primary_key=True, autoincrement=True)
    nombre_tipo_catalogo = Column(String(100), nullable=False)
    
    def __repr__(self):
        return f"<TipoCatalogoORM(id={self.id_tipo_catalogo}, nombre={self.nombre_tipo_catalogo})>"
