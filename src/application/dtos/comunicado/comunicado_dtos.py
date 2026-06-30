from datetime import date
from typing import Optional
from pydantic import BaseModel


class CreateComunicadoRequest(BaseModel):
    doi: str
    num_comunicado: str
    id_emisor: int
    fecha_recepcion: date
    id_destinatario: int
    fecha_registro: date
    id_registro: int
    id_metodo_recepcion: int
    tema: str
    id_tipo_comunicado: int
    observaciones: Optional[str] = None


class UpdateComunicadoRequest(BaseModel):
    doi: str
    num_comunicado: str
    id_emisor: int
    fecha_recepcion: date
    id_destinatario: int
    fecha_registro: date
    id_registro: int
    id_metodo_recepcion: int
    tema: str
    id_tipo_comunicado: int
    observaciones: Optional[str] = None


class ComunicadoResponse(BaseModel):
    id_comunicado: int
    doi: str
    num_comunicado: str
    id_emisor: int
    fecha_recepcion: date
    id_destinatario: int
    fecha_registro: date
    id_registro: int
    id_metodo_recepcion: int
    tema: str
    id_tipo_comunicado: int
    observaciones: Optional[str] = None


class ListComunicadoResponse(BaseModel):
    items: list[ComunicadoResponse]
    total: int
    skip: int
    limit: int
