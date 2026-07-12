from typing import List
from src.domain.entities.rol_empleado import RolEmpleado
from src.domain.ports.input.rol_empleado import (
    CreateRolEmpleadoInputPort,
    GetRolEmpleadoInputPort,
    ListRolEmpleadoInputPort,
    UpdateRolEmpleadoInputPort,
    DeleteRolEmpleadoInputPort,
)
from src.domain.ports.output.rol_empleado import RolEmpleadoRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException


class CreateRolEmpleadoUseCase(CreateRolEmpleadoInputPort):
    def __init__(self, repository: RolEmpleadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, descripcion: str) -> RolEmpleado:
        entity = RolEmpleado.crear(descripcion)
        return self.repository.crear(entity)


class GetRolEmpleadoUseCase(GetRolEmpleadoInputPort):
    def __init__(self, repository: RolEmpleadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_rol: int) -> RolEmpleado:
        resultado = self.repository.obtener_por_id(id_rol)
        if not resultado:
            raise RecursoNoEncontradoException(f"RolEmpleado {id_rol} no encontrado.")
        return resultado


class ListRolEmpleadoUseCase(ListRolEmpleadoInputPort):
    def __init__(self, repository: RolEmpleadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, skip: int = 0, limit: int = 50) -> List[RolEmpleado]:
        return self.repository.listar(skip, limit)


class UpdateRolEmpleadoUseCase(UpdateRolEmpleadoInputPort):
    def __init__(self, repository: RolEmpleadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_rol: int, descripcion: str) -> RolEmpleado:
        existente = self.repository.obtener_por_id(id_rol)
        if not existente:
            raise RecursoNoEncontradoException(f"RolEmpleado {id_rol} no encontrado.")
        existente.descripcion = descripcion
        return self.repository.actualizar(existente)


class DeleteRolEmpleadoUseCase(DeleteRolEmpleadoInputPort):
    def __init__(self, repository: RolEmpleadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, id_rol: int) -> None:
        existente = self.repository.obtener_por_id(id_rol)
        if not existente:
            raise RecursoNoEncontradoException(f"RolEmpleado {id_rol} no encontrado.")
        self.repository.eliminar(id_rol)