from dataclasses import dataclass


@dataclass
class RolResponsable:
    """Entidad de dominio RolResponsable.
    
    Representa un rol que puede tener un responsable de tarea.
    Ejemplos: Supervisor, Técnico, Administrador.
    """
    id_rol: int
    descripcion_rol: str