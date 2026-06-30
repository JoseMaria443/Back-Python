"""Modelo SQLAlchemy para la entidad Empleado."""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from src.infrastructure.config.database import Base


class EmpleadoModel(Base):
    """Modelo de tabla empleado."""
    
    __tablename__ = "empleados"
    
    id_empleado = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    id_area = Column(Integer, ForeignKey("areas.id_area"), nullable=False)
    id_cargo = Column(Integer, ForeignKey("cargos.id_cargo"), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    activo = Column(Integer, default=1)  # 1=activo, 0=inactivo
    
    # Relaciones
    # area = relationship("AreaModel", back_populates="empleados")
    # cargo = relationship("CargoModel", back_populates="empleados")
    # emp_cargos = relationship("EmpCargoModel", back_populates="empleado")
    # tareas_responsable = relationship("TareaResponsableModel", back_populates="empleado")
    # comunicados_destinatario = relationship("ComunicadoDestinatarioModel", back_populates="empleado")
    
    def __repr__(self):
        return f"<EmpleadoModel(id_empleado={self.id_empleado}, email={self.email})>"