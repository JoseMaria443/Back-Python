from pydantic import BaseModel


class AsociarTareaArchivoRequest(BaseModel):
    id_archivo: int


class TareaArchivoResponse(BaseModel):
    id_tarea: int
    id_archivo: int
