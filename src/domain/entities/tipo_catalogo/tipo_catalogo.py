from dataclasses import dataclass


@dataclass
class TipoCatalogo:
    """Entidad de dominio TipoCatalogo.
    
    Define los tipos de catálogos existentes.
    Ejemplos: TipoComunicado, MetodoRecepcion.
    """
    id_tipo_catalogo: int
    nombre_tipo_catalogo: str
