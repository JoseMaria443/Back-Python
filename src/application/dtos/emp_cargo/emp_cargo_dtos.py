from datetime import date

from pydantic import BaseModel, Field


class AsociarEmpCargoRequest(BaseModel):
    id_empleado: int = Field(..., gt=0)
    id_cargo: int = Field(..., gt=0)
    fecha_inicio: date
    fecha_termina: date
    id_registro_modificacion: int = Field(..., gt=0)


class EmpCargoResponse(BaseModel):
    id_empleado: int
    id_cargo: int
    fecha_inicio: date
    fecha_termina: date
    id_registro_modificacion: int