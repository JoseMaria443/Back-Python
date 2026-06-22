from dataclasses import dataclass


@dataclass
class RolResponsable:
    """Entidad de dominio Rol_Responsable.
    
    Catálogo separado para roles de responsables en Tarea_Responsable.
    """
    id_rol: int
    descripcion_rol: str
