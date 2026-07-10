from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from .base import Base


class HistorialEstadoEmpleadoORM(Base):
    __tablename__ = "historial_estado_empleado"

    id_historial = Column(Integer, primary_key=True, autoincrement=True)
    id_empleado = Column(Integer, ForeignKey('empleado.id_empleado'), nullable=False)
    accion = Column(String(50), nullable=False)
    id_empleado_ejecutor = Column(Integer, ForeignKey('empleado.id_empleado'), nullable=False)
    fecha = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<HistorialEstadoEmpleadoORM(id={self.id_historial}, accion={self.accion})>"