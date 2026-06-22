from dataclasses import dataclass


@dataclass
class TareaResponsable:
    """Entidad de dominio TareaResponsable.
    
    Asociativa entre Tarea y Empleado (responsable), con rol.
    """
    id_tarea: int
    id_responsable: int
    id_rol: int
