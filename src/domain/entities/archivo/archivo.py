from dataclasses import dataclass
from datetime import date


@dataclass
class Archivo:
    """Entidad de dominio Archivo.
    
    Representa un archivo (documento, evidencia) en el sistema.
    Puede ser adjunto de un Comunicado o de una Tarea.
    """
    id_archivo: int
    doi: str
    descripcion: str
    url_archivo: str
    nombre_original: str
    id_elaborador: int
    fecha_registro: date
