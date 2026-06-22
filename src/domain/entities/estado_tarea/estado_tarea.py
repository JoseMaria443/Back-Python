from dataclasses import dataclass


@dataclass
class EstadoTarea:
    """Entidad de dominio EstadoTarea.
    
    Catálogo específico para estados de Tarea.
    Ejemplos: Asignada, Cancelada, Pospuesta, Entregada, Rechazada, Terminada.
    """
    id_estado_tarea: int
    nombre_estado: str
