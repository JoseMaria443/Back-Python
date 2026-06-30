from pydantic import BaseModel


class AsociarComunicadoAdjuntoRequest(BaseModel):
    id_archivo: int


class ComunicadoAdjuntoResponse(BaseModel):
    id_comunicado: int
    id_archivo: int
