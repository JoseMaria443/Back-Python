from dataclasses import dataclass


@dataclass
class ComunicadoDestinatario:
    """Entidad de dominio ComunicadoDestinatario.
    
    Asociativa entre Comunicado y Destinatario, con rol específico.
    """
    id_comunicado: int
    id_destinatario: int
    id_rol_destinatario: int
