from dataclasses import dataclass


@dataclass
class Estado:
    """Entidad de dominio Estado.
    
    Representa un estado base del sistema.
    Ejemplos: Activo, Inactivo, Pendiente.
    """
    id_estado: int
    nombre_estado: str
