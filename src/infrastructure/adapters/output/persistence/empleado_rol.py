from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime
from .base import Base


class EmpleadoRolORM(Base):
    __tablename__ = "empleado_rol"
    
    id_empleado = Column(Integer, ForeignKey("empleado.id_empleado"), primary_key=True)
    id_rol = Column(Integer, ForeignKey("rol_empleado.id_rol"), primary_key=True)
    fecha_asignacion = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<EmpleadoRolORM(emp={self.id_empleado}, rol={self.id_rol})>"