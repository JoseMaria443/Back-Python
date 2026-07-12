from dataclasses import dataclass


@dataclass
class RolEmpleado:
    """Entidad de dominio RolEmpleado.
    
    Catálogo de roles de sistema para empleados.
    Define permisos globales del empleado en el sistema.
    Ejemplos: Administrador, Supervisor, Operador, RH.
    """
    id_rol: int
    descripcion: str

    @staticmethod
    def crear(descripcion: str) -> "RolEmpleado":
        """Factory method para crear un nuevo rol."""
        return RolEmpleado(
            id_rol=0,
            descripcion=descripcion,
        )