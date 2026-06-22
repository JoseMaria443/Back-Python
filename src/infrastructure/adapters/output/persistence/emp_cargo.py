from sqlalchemy import Column, Integer, Date, ForeignKey
from .base import Base


class EmpCargoORM(Base):
    """Modelo ORM: EmpCargo.
    
    Historial de cargos de un empleado con fechas.
    """
    __tablename__ = "emp_cargo"
    
    id_empleado = Column(Integer, ForeignKey("empleado.id_empleado"), primary_key=True)
    id_cargo = Column(Integer, primary_key=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_termina = Column(Date, nullable=False)
    id_registro_modificacion = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"<EmpCargoORM(emp={self.id_empleado}, cargo={self.id_cargo})>"