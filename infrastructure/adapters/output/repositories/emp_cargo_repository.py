from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.emp_cargo import EmpCargo
from src.domain.ports.output.emp_cargo import EmpCargoRepositoryPort
from src.infrastructure.adapters.output.models.emp_cargo_model import EmpCargoModel


class EmpCargoRepository(EmpCargoRepositoryPort):
    def __init__(self, db: Session):
        self.db = db
    
    def crear(self, emp_cargo: EmpCargo) -> EmpCargo:
        db_emp_cargo = EmpCargoModel(
            id_empleado=emp_cargo.id_empleado,
            id_cargo=emp_cargo.id_cargo,
            fecha_inicio=emp_cargo.fecha_inicio,
            fecha_termina=emp_cargo.fecha_termina,
            id_registro_modificacion=emp_cargo.id_registro_modificacion,
        )
        self.db.add(db_emp_cargo)
        self.db.commit()
        self.db.refresh(db_emp_cargo)
        return self._to_entity(db_emp_cargo)
    
    def obtener_por_id(self, id_empleado: int, id_cargo: int) -> Optional[EmpCargo]:
        db_emp_cargo = self.db.query(EmpCargoModel).filter(
            EmpCargoModel.id_empleado == id_empleado,
            EmpCargoModel.id_cargo == id_cargo,
        ).first()
        return self._to_entity(db_emp_cargo) if db_emp_cargo else None
    
    def listar(self, skip: int = 0, limit: int = 50) -> List[EmpCargo]:
        db_emp_cargos = self.db.query(EmpCargoModel).offset(skip).limit(limit).all()
        return [self._to_entity(ec) for ec in db_emp_cargos]
    
    def actualizar(self, emp_cargo: EmpCargo) -> EmpCargo:
        db_emp_cargo = self.db.query(EmpCargoModel).filter(
            EmpCargoModel.id_empleado == emp_cargo.id_empleado,
            EmpCargoModel.id_cargo == emp_cargo.id_cargo,
        ).first()
        if db_emp_cargo:
            db_emp_cargo.fecha_inicio = emp_cargo.fecha_inicio
            db_emp_cargo.fecha_termina = emp_cargo.fecha_termina
            db_emp_cargo.id_registro_modificacion = emp_cargo.id_registro_modificacion
            self.db.commit()
            self.db.refresh(db_emp_cargo)
            return self._to_entity(db_emp_cargo)
        return None
    
    def eliminar(self, id_empleado: int, id_cargo: int) -> bool:
        db_emp_cargo = self.db.query(EmpCargoModel).filter(
            EmpCargoModel.id_empleado == id_empleado,
            EmpCargoModel.id_cargo == id_cargo,
        ).first()
        if db_emp_cargo:
            self.db.delete(db_emp_cargo)
            self.db.commit()
            return True
        return False
    
    def _to_entity(self, model: EmpCargoModel) -> EmpCargo:
        return EmpCargo(
            id_empleado=model.id_empleado,
            id_cargo=model.id_cargo,
            fecha_inicio=model.fecha_inicio,
            fecha_termina=model.fecha_termina,
            id_registro_modificacion=model.id_registro_modificacion,
        )