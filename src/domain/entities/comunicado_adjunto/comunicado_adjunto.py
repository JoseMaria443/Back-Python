from dataclasses import dataclass


@dataclass
class ComunicadoAdjunto:
    """Entidad de dominio Comunicado_Adjunto.
    
    Asociativa entre Comunicado y Archivo. Un Comunicado puede tener varios archivos adjuntos.
    """
    id_comunicado: int
    id_archivo: int
