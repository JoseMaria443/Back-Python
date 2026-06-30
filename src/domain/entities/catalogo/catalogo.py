from dataclasses import dataclass


@dataclass
class Catalogo:
    """Entidad de dominio Catalogo.
    
    Representa un catálogo de valores que pertenece a un tipo de catálogo.
    Ejemplos: Áreas, Cargos, Tipos de Documento.
    """
    id_catalogo: int
    nombre_catalogo: str
    id_tipo_catalogo: int
    descripcion: str = None