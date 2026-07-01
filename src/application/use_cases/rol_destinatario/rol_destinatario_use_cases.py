from typing import List
from src.domain.entities.rol_destinatario import RolDestinatario
from src.domain.ports.input.rol_destinatario import (
    CreateRolDestinatarioInputPort,
    GetRolDestinatarioInputPort,
    ListRolDestinatarioInputPort,
    UpdateRolDestinatarioInputPort,
    DeleteRolDestinatarioInputPort,
)
from src.domain.ports.output.rol_destinatario import RolDestinatarioRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException


class CreateRolDestinatarioUseCase(CreateRolDestinatarioInputPort):
    def __init__(self, repository: RolDestinatarioRepositoryPort):
        self.repository = repository

    def ejecutar(self, descripcion: str) -> RolDestinatario:
        rol = RolDestinatario(
            id_rol=0,
            descripcion=descripcion,
        )
        return self.repository.crear(rol)


class GetRolDestinatarioUseCase(GetRolDestinatarioInputPort):
    def __init__(self, repository: RolDestinatarioRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_rol: int) -> RolDestinatario:
        resultado = self.repository.obtener_por_id(id_rol)
        if not resultado:
            raise RecursoNoEncontradoException(f"RolDestinatario {id_rol} no encontrado.")
        return resultado


class ListRolDestinatarioUseCase(ListRolDestinatarioInputPort):
    def __init__(self, repository: RolDestinatarioRepositoryPort):
        self.repository = repository

    def ejecutar(self, skip: int = 0, limit: int = 50) -> List[RolDestinatario]:
        return self.repository.listar(skip, limit)


class UpdateRolDestinatarioUseCase(UpdateRolDestinatarioInputPort):
    def __init__(self, repository: RolDestinatarioRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_rol: int, descripcion: str) -> RolDestinatario:
        existente = self.repository.obtener_por_id(id_rol)
        if not existente:
            raise RecursoNoEncontradoException(f"RolDestinatario {id_rol} no encontrado.")
        existente.descripcion = descripcion
        actualizado = self.repository.actualizar(existente)
        return actualizado


class DeleteRolDestinatarioUseCase(DeleteRolDestinatarioInputPort):
    def __init__(self, repository: RolDestinatarioRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_rol: int) -> None:
        existente = self.repository.obtener_por_id(id_rol)
        if not existente:
            raise RecursoNoEncontradoException(f"RolDestinatario {id_rol} no encontrado.")
        self.repository.eliminar(id_rol)