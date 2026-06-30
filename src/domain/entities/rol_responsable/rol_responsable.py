from dataclasses import dataclass


@dataclass
class RolResponsable:
    """Entidad de dominio RolResponsable.
    
    Representa un rol que puede tener un responsable de tarea.
    Ejemplos: Supervisor, Técnico, Administrador.
    """
    id_rol_responsable: int
    nombre_rol: str
    descripcion: str = None