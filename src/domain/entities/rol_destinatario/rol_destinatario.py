from dataclasses import dataclass


@dataclass
class RolDestinatario:
    """Entidad de dominio RolDestinatario.
    
    Representa un rol que puede tener un destinatario de comunicado.
    Ejemplos: Jefe, Subalterno, RRHH.
    """
    id_rol: int
    descripcion: str