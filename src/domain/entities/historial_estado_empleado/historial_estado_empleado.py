from dataclasses import dataclass
from datetime import datetime


@dataclass
class HistorialEstadoEmpleado:
    id_historial: int
    id_empleado: int
    accion: str
    id_empleado_ejecutor: int
    fecha: datetime

    @staticmethod
    def crear(
        id_empleado: int,
        accion: str,
        id_empleado_ejecutor: int,
    ) -> "HistorialEstadoEmpleado":
        return HistorialEstadoEmpleado(
            id_historial=0,
            id_empleado=id_empleado,
            accion=accion,
            id_empleado_ejecutor=id_empleado_ejecutor,
            fecha=datetime.now(),
        )