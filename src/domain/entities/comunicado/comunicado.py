from dataclasses import dataclass
from typing import Optional


@dataclass
class Comunicado:
    """Entidad de dominio Comunicado.
    
    Representa un comunicado (antes Oficio) sin campo directo IdArchivo.
    Los archivos adjuntos se acceden a través de la asociativa Comunicado_adjunto.
    """
    id_comunicado: int
    doi: str
    num_comunicado: str
    id_emisor: int
    fecha_recepcion: "date"
    id_destinatario: int
    fecha_registro: "date"
    id_registro: int
    id_metodo_recepcion: int
    tema: str
    id_tipo_comunicado: int
    observaciones: Optional[str] = None
