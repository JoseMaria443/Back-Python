from dataclasses import dataclass
from datetime import datetime


@dataclass
class RolEmpleado:
    id_rol: int
    descripcion: str

    @staticmethod
    def crear(descripcion: str) -> "RolEmpleado":
        return RolEmpleado(
            id_rol=0,
            descripcion=descripcion,
        )