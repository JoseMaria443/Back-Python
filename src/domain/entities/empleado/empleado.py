from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Empleado:
    """Entidad de dominio Empleado.
    
    Representa un empleado del sistema con datos básicos y relaciones a área y cargo.
    """
    id_empleado: int
    nombre: str
    email: str
    password_hash: str
    id_area: int
    id_cargo: int
    
    @staticmethod
    def crear(
        nombre: str,
        email: str,
        password_hash: str,
        id_area: int,
        id_cargo: int,
    ) -> "Empleado":
        """Factory method para crear una nueva instancia de Empleado."""
        return Empleado(
            id_empleado=0,  # Será asignado por la BD
            nombre=nombre,
            email=email,
            password_hash=password_hash,
            id_area=id_area,
            id_cargo=id_cargo,
        )
