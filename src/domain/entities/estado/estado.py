from dataclasses import dataclass
from typing import Optional


@dataclass
class Estado:
    """Entidad de dominio Estado (genérico).
    
    Catálogo genérico para estados de otras entidades (Comunicado, Archivo, etc.).
    NO se usa para Tarea (ver EstadoTarea).
    Estructura definitiva pendiente.
    """
    id_estado: int
    nombre_estado: str
