from typing import List
from src.domain.entities.rol_empleado import RolEmpleado
from src.domain.entities.empleado_rol import EmpleadoRol
from src.domain.ports.input.rol_empleado import (
    CreateRolEmpleadoInputPort,
    ListRolEmpleadoInputPort,
    UpdateRolEmpleadoInputPort,
    DeleteRolEmpleadoInputPort,
    AsignarRolEmpleadoInputPort,
    QuitarRolEmpleadoInputPort,
    ListarRolesEmpleadoInputPort,
)
from src.domain.ports.output.rol_empleado import RolEmpleadoRepositoryPort
from src.domain.ports.output.empleado_rol import EmpleadoRolRepositoryPort
from src.domain.exceptions.crud_exceptions import RecursoNoEncontradoException, RecursoEnUsoException, AsociacionYaExisteException


class CreateRolEmpleadoUseCase(CreateRolEmpleadoInputPort):
    def __init__(self, repository: RolEmpleadoRepositoryPort):
        self.repository = repository

    def ejecutar(self, descripcion: str) -> RolEmpleado:
        entity = RolEmpleado.crear(descripcion)
        return self.repository.crear(entity)


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
        if self.repository.existe_asignado(id_rol):
            raise RecursoEnUsoException(
                f"No se puede eliminar el rol {id_rol} porque está asignado a empleados."
            )
        if not self.repository.eliminar(id_rol):
            raise RecursoNoEncontradoException(f"RolEmpleado {id_rol} no encontrado.")


class AsignarRolEmpleadoUseCase(AsignarRolEmpleadoInputPort):
    def __init__(self, empleado_rol_repo: EmpleadoRolRepositoryPort, rol_repo: RolEmpleadoRepositoryPort):
        self.empleado_rol_repo = empleado_rol_repo
        self.rol_repo = rol_repo

    def ejecutar(self, id_empleado: int, id_rol: int) -> RolEmpleado:
        if not self.rol_repo.obtener_por_id(id_rol):
            raise RecursoNoEncontradoException(f"RolEmpleado {id_rol} no encontrado.")
        if self.empleado_rol_repo.existe(id_empleado, id_rol):
            raise AsociacionYaExisteException(
                f"El empleado {id_empleado} ya tiene asignado el rol {id_rol}."
            )
        self.empleado_rol_repo.asignar(id_empleado, id_rol)
        return self.rol_repo.obtener_por_id(id_rol)


class QuitarRolEmpleadoUseCase(QuitarRolEmpleadoInputPort):
    def __init__(self, empleado_rol_repo: EmpleadoRolRepositoryPort):
        self.empleado_rol_repo = empleado_rol_repo

    def ejecutar(self, id_empleado: int, id_rol: int) -> None:
        if not self.empleado_rol_repo.existe(id_empleado, id_rol):
            raise RecursoNoEncontradoException(
                f"El empleado {id_empleado} no tiene asignado el rol {id_rol}."
            )
        self.empleado_rol_repo.quitar(id_empleado, id_rol)


class ListarRolesEmpleadoUseCase(ListarRolesEmpleadoInputPort):
    def __init__(self, empleado_rol_repo: EmpleadoRolRepositoryPort):
        self.empleado_rol_repo = empleado_rol_repo

    def ejecutar(self, id_empleado: int) -> List[RolEmpleado]:
        return self.empleado_rol_repo.listar_por_empleado(id_empleado)