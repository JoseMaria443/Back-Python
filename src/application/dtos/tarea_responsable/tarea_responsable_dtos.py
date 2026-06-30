from pydantic import BaseModel


class AsociarTareaResponsableRequest(BaseModel):
    id_responsable: int
    id_rol: int


class TareaResponsableResponse(BaseModel):
    id_tarea: int
    id_responsable: int
    id_rol: int
