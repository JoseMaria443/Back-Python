from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RolDestinatarioORM(Base):
    """Modelo ORM: Rol_Destinatario.
    
    Catálogo separado para roles de destinatarios.
    """
    __tablename__ = "rol_destinatario"
    
    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(255), nullable=False)
    
    def __repr__(self):
        return f"<RolDestinatarioORM(id={self.id_rol}, desc={self.descripcion})>"
