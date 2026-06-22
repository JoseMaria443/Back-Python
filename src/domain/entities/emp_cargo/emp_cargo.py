from dataclasses import dataclass
from datetime import date


@dataclass
class EmpCargo:
    """Entidad de dominio EmpCargo.
    
    Historial de cargos de un empleado con fechas de inicio y término.
    """
    id_empleado: int
    id_cargo: int
    fecha_inicio: date
    fecha_termina: date
    id_registro_modificacion: int
