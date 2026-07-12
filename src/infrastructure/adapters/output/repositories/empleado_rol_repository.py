from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.empleado_rol import EmpleadoRol
from src.domain.entities.rol_empleado import RolEmpleado
from src.domain.ports.output.empleado_rol import EmpleadoRolRepositoryPort
from src.infrastructure.adapters.output.persistence.empleado_rol import EmpleadoRolORM


class EmpleadoRolRepository(EmpleadoRolRepositoryPort):
    def __init__(self, session: Session):
        self.session = session

    def asignar(self, id_empleado: int, id_rol: int) -> EmpleadoRol:
        orm = EmpleadoRolORM(
            id_empleado=id_empleado,
            id_rol=id_rol,
        )
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return EmpleadoRol(
            id_empleado=orm.id_empleado,
            id_rol=orm.id_rol,
            fecha_asignacion=orm.fecha_asignacion,
        )

    def quitar(self, id_empleado: int, id_rol: int) -> bool:
        orm = self.session.query(EmpleadoRolORM).filter(
            EmpleadoRolORM.id_empleado == id_empleado,
            EmpleadoRolORM.id_rol == id_rol,
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True

    def listar_por_empleado(self, id_empleado: int) -> List[RolEmpleado]:
        from src.infrastructure.adapters.output.persistence.rol_empleado import RolEmpleadoORM
        orms = self.session.query(RolEmpleadoORM).join(
            EmpleadoRolORM,
            RolEmpleadoORM.id_rol == EmpleadoRolORM.id_rol
        ).filter(
            EmpleadoRolORM.id_empleado == id_empleado
        ).all()
        return [
            RolEmpleado(
                id_rol=orm.id_rol,
                descripcion=orm.descripcion,
            )
            for orm in orms
        ]

    def existe(self, id_empleado: int, id_rol: int) -> bool:
        count = self.session.query(EmpleadoRolORM).filter(
            EmpleadoRolORM.id_empleado == id_empleado,
            EmpleadoRolORM.id_rol == id_rol,
        ).count()
        return count > 0