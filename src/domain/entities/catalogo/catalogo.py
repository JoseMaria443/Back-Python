from dataclasses import dataclass


@dataclass
class Catalogo:
    """Entidad de dominio Catalogo.
    
    Catálogo genérico que agrupa tipos de datos comunes como
    TipoComunicado, MetodoRecepcion, etc.
    """
    id_catalogo: int
    id_tipo_catalogo: int
    descripcion: str
