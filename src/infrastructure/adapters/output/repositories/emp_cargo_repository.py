from typing import Optional
from sqlalchemy.orm import Session
from src.domain.entities.emp_cargo import EmpCargo
from src.domain.ports.output.emp_cargo import EmpCargoRepositoryPort
from src.infrastructure.adapters.output.persistence.emp_cargo import EmpCargoORM


class EmpCargoRepository(EmpCargoRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, emp_cargo: EmpCargo) -> EmpCargo:
        orm = EmpCargoORM(
            id_empleado=emp_cargo.id_empleado,
            id_cargo=emp_cargo.id_cargo,
            fecha_inicio=emp_cargo.fecha_inicio,
            fecha_termina=emp_cargo.fecha_termina,
            id_registro_modificacion=emp_cargo.id_registro_modificacion,
        )
        self.session.add(orm)
        self.session.commit()
        return emp_cargo

    def obtener(self, id_empleado: int, id_cargo: int) -> Optional[EmpCargo]:
        orm = self.session.query(EmpCargoORM).filter(
            EmpCargoORM.id_empleado == id_empleado,
            EmpCargoORM.id_cargo == id_cargo,
        ).first()
        if not orm:
            return None
        return EmpCargo(
            id_empleado=orm.id_empleado,
            id_cargo=orm.id_cargo,
            fecha_inicio=orm.fecha_inicio,
            fecha_termina=orm.fecha_termina,
            id_registro_modificacion=orm.id_registro_modificacion,
        )

    def eliminar(self, id_empleado: int, id_cargo: int) -> bool:
        orm = self.session.query(EmpCargoORM).filter(
            EmpCargoORM.id_empleado == id_empleado,
            EmpCargoORM.id_cargo == id_cargo,
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True
