from pydantic import BaseModel


class AsociarComunicadoDestinatarioRequest(BaseModel):
    id_destinatario: int
    id_rol_destinatario: int


class ComunicadoDestinatarioResponse(BaseModel):
    id_comunicado: int
    id_destinatario: int
    id_rol_destinatario: int
