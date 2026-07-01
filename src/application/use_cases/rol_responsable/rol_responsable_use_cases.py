from typing import List
from src.domain.entities.rol_responsable import RolResponsable
from src.domain.ports.input.rol_responsable import (
    CreateRolResponsableInputPort,
    GetRolResponsableInputPort,
    ListRolResponsableInputPort,
    UpdateRolResponsableInputPort,
    DeleteRolResponsableInputPort,
)
from src.domain.ports.output.rol_responsable import RolResponsableRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException


class CreateRolResponsableUseCase(CreateRolResponsableInputPort):
    def __init__(self, repository: RolResponsableRepositoryPort):
        self.repository = repository

    def ejecutar(self, descripcion_rol: str) -> RolResponsable:
        rol = RolResponsable(
            id_rol=0,
            descripcion_rol=descripcion_rol,
        )
        return self.repository.crear(rol)


class GetRolResponsableUseCase(GetRolResponsableInputPort):
    def __init__(self, repository: RolResponsableRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_rol: int) -> RolResponsable:
        resultado = self.repository.obtener_por_id(id_rol)
        if not resultado:
            raise RecursoNoEncontradoException(f"RolResponsable {id_rol} no encontrado.")
        return resultado


class ListRolResponsableUseCase(ListRolResponsableInputPort):
    def __init__(self, repository: RolResponsableRepositoryPort):
        self.repository = repository

    def ejecutar(self, skip: int = 0, limit: int = 50) -> List[RolResponsable]:
        return self.repository.listar(skip, limit)


class UpdateRolResponsableUseCase(UpdateRolResponsableInputPort):
    def __init__(self, repository: RolResponsableRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_rol: int, descripcion_rol: str) -> RolResponsable:
        existente = self.repository.obtener_por_id(id_rol)
        if not existente:
            raise RecursoNoEncontradoException(f"RolResponsable {id_rol} no encontrado.")
        existente.descripcion_rol = descripcion_rol
        actualizado = self.repository.actualizar(existente)
        return actualizado


class DeleteRolResponsableUseCase(DeleteRolResponsableInputPort):
    def __init__(self, repository: RolResponsableRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_rol: int) -> None:
        existente = self.repository.obtener_por_id(id_rol)
        if not existente:
            raise RecursoNoEncontradoException(f"RolResponsable {id_rol} no encontrado.")
        self.repository.eliminar(id_rol)