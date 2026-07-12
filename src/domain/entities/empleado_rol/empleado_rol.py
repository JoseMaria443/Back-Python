from dataclasses import dataclass
from datetime import datetime


@dataclass
class EmpleadoRol:
    id_empleado: int
    id_rol: int
    fecha_asignacion: datetime

    @staticmethod
    def crear(id_empleado: int, id_rol: int) -> "EmpleadoRol":
        return EmpleadoRol(
            id_empleado=id_empleado,
            id_rol=id_rol,
            fecha_asignacion=datetime.utcnow(),
        )