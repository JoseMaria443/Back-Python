from dataclasses import dataclass


@dataclass
class TareaArchivo:
    """Entidad de dominio TareaArchivo.
    
    Asociativa entre Tarea y Archivo.
    Una tarea puede tener múltiples archivos adjuntos.
    """
    id_tarea: int
    id_archivo: int
