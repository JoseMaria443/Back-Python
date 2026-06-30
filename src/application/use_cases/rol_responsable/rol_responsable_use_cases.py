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

    def ejecutar(self, nombre_rol: str, descripcion: str = None) -> RolResponsable:
        rol = RolResponsable(
            id_rol_responsable=0,
            nombre_rol=nombre_rol,
            descripcion=descripcion,
        )
        return self.repository.crear(rol)


class GetRolResponsableUseCase(GetRolResponsableInputPort):
    def __init__(self, repository: RolResponsableRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_rol_responsable: int) -> RolResponsable:
        resultado = self.repository.obtener_por_id(id_rol_responsable)
        if not resultado:
            raise RecursoNoEncontradoException(f"RolResponsable {id_rol_responsable} no encontrado.")
        return resultado


class ListRolResponsableUseCase(ListRolResponsableInputPort):
    def __init__(self, repository: RolResponsableRepositoryPort):
        self.repository = repository

    def ejecutar(self, skip: int = 0, limit: int = 50) -> List[RolResponsable]:
        return self.repository.listar(skip, limit)


class UpdateRolResponsableUseCase(UpdateRolResponsableInputPort):
    def __init__(self, repository: RolResponsableRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_rol_responsable: int, nombre_rol: str, descripcion: str = None) -> RolResponsable:
        existente = self.repository.obtener_por_id(id_rol_responsable)
        if not existente:
            raise RecursoNoEncontradoException(f"RolResponsable {id_rol_responsable} no encontrado.")
        existente.nombre_rol = nombre_rol
        existente.descripcion = descripcion
        actualizado = self.repository.actualizar(existente)
        return actualizado


class DeleteRolResponsableUseCase(DeleteRolResponsableInputPort):
    def __init__(self, repository: RolResponsableRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_rol_responsable: int) -> None:
        existente = self.repository.obtener_por_id(id_rol_responsable)
        if not existente:
            raise RecursoNoEncontradoException(f"RolResponsable {id_rol_responsable} no encontrado.")
        self.repository.eliminar(id_rol_responsable)