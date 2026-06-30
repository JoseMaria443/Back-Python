from sqlalchemy import Column, Integer, ForeignKey, Date, DateTime
from datetime import datetime
from src.infrastructure.config.database import Base


class EmpCargoModel(Base):
    __tablename__ = "emp_cargos"
    
    id_empleado = Column(Integer, ForeignKey("empleados.id_empleado"), primary_key=True)
    id_cargo = Column(Integer, ForeignKey("cargos.id_cargo"), primary_key=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_termina = Column(Date, nullable=False)
    id_registro_modificacion = Column(Integer, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)