from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.rol_empleado import RolEmpleado
from src.domain.ports.output.rol_empleado import RolEmpleadoRepositoryPort
from src.infrastructure.adapters.output.persistence.rol_empleado import RolEmpleadoORM


class RolEmpleadoRepository(RolEmpleadoRepositoryPort):
    """Implementación del repositorio de RolEmpleado."""

    def __init__(self, session: Session):
        self.session = session

    def crear(self, rol: RolEmpleado) -> RolEmpleado:
        orm = RolEmpleadoORM(descripcion=rol.descripcion)
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return RolEmpleado(
            id_rol=orm.id_rol,
            descripcion=orm.descripcion,
        )

    def obtener_por_id(self, id_rol: int) -> Optional[RolEmpleado]:
        orm = self.session.query(RolEmpleadoORM).filter(
            RolEmpleadoORM.id_rol == id_rol
        ).first()
        if not orm:
            return None
        return RolEmpleado(
            id_rol=orm.id_rol,
            descripcion=orm.descripcion,
        )

    def listar(self, skip: int = 0, limit: int = 50) -> List[RolEmpleado]:
        orms = self.session.query(RolEmpleadoORM).offset(skip).limit(limit).all()
        return [
            RolEmpleado(
                id_rol=orm.id_rol,
                descripcion=orm.descripcion,
            )
            for orm in orms
        ]

    def contar(self) -> int:
        return self.session.query(RolEmpleadoORM).count()

    def actualizar(self, rol: RolEmpleado) -> Optional[RolEmpleado]:
        orm = self.session.query(RolEmpleadoORM).filter(
            RolEmpleadoORM.id_rol == rol.id_rol
        ).first()
        if not orm:
            return None
        orm.descripcion = rol.descripcion
        self.session.commit()
        self.session.refresh(orm)
        return RolEmpleado(
            id_rol=orm.id_rol,
            descripcion=orm.descripcion,
        )

    def eliminar(self, id_rol: int) -> bool:
        orm = self.session.query(RolEmpleadoORM).filter(
            RolEmpleadoORM.id_rol == id_rol
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True