from sqlalchemy import Column, Integer, String
from .base import Base


class RolEmpleadoORM(Base):
    """Modelo ORM: RolEmpleado.
    
    Catálogo de roles de sistema para empleados.
    """
    __tablename__ = "rol_empleado"
    
    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(255), nullable=False)
    
    def __repr__(self):
        return f"<RolEmpleadoORM(id={self.id_rol}, desc={self.descripcion})>"