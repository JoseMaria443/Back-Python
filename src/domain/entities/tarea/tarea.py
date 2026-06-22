from dataclasses import dataclass
from typing import Optional


@dataclass
class Tarea:
    """Entidad de dominio Tarea.
    
    Representa una tarea derivada de un comunicado, con estado específico en EstadoTarea.
    """
    id_tarea: int
    id_comunicado: int
    descripcion: str
    fecha_entrega: "date"
    fecha_registro: "date"
    id_estado_tarea: Optional[int] = None
