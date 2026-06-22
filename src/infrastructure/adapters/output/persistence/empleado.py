from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Date
from datetime import datetime
from .base import Base


class EmpleadoORM(Base):
    """Modelo ORM: Empleado.
    
    Mapeo a tabla PostgreSQL 'empleado' con soporte para autenticación.
    """
    __tablename__ = "empleado"
    
    id_empleado = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    id_area = Column(Integer, nullable=False)
    id_cargo = Column(Integer, nullable=False)
    # ForeignKey pendientes: id_area -> Area, id_cargo -> Cargo
    
    def __repr__(self):
        return f"<EmpleadoORM(id={self.id_empleado}, email={self.email})>"
