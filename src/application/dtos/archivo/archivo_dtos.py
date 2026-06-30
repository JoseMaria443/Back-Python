from datetime import date
from pydantic import BaseModel


class CreateArchivoRequest(BaseModel):
    doi: str
    descripcion: str
    url_archivo: str
    nombre_original: str
    id_elaborador: int
    fecha_registro: date


class UpdateArchivoRequest(BaseModel):
    doi: str
    descripcion: str
    url_archivo: str
    nombre_original: str
    id_elaborador: int
    fecha_registro: date


class ArchivoResponse(BaseModel):
    id_archivo: int
    doi: str
    descripcion: str
    url_archivo: str
    nombre_original: str
    id_elaborador: int
    fecha_registro: date


class ListArchivoResponse(BaseModel):
    items: list[ArchivoResponse]
    total: int
    skip: int
    limit: int
