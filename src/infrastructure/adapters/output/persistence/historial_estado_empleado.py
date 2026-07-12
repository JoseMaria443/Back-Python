from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from .base import Base


class HistorialEstadoEmpleadoORM(Base):
    """Modelo ORM: HistorialEstadoEmpleado.
    
    Registra el historial de cambios de estado de un empleado.
    """
    __tablename__ = "historial_estado_empleado"
    
    id_historial = Column(Integer, primary_key=True, autoincrement=True)
    id_empleado = Column(Integer, ForeignKey("empleado.id_empleado"), nullable=False)
    accion = Column(String(50), nullable=False)
    id_empleado_ejecutor = Column(Integer, ForeignKey("empleado.id_empleado"), nullable=False)
    fecha = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<HistorialEstadoEmpleadoORM(id={self.id_historial}, empleado={self.id_empleado}, accion={self.accion})>"