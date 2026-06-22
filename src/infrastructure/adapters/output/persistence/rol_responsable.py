from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RolResponsableORM(Base):
    """Modelo ORM: Rol_Responsable.
    
    Catálogo separado para roles de responsables en tareas.
    """
    __tablename__ = "rol_responsable"
    
    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    descripcion_rol = Column(String(255), nullable=False)
    
    def __repr__(self):
        return f"<RolResponsableORM(id={self.id_rol}, desc={self.descripcion_rol})>"
