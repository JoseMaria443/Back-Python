from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.empleado import Empleado
from src.domain.ports.output.empleado import EmpleadoRepositoryPort
from src.infrastructure.adapters.output.models.empleado_model import EmpleadoModel
from src.infrastructure.config.security import hash_password, verify_password


class EmpleadoRepository(EmpleadoRepositoryPort):
    def __init__(self, db: Session):
        self.db = db
    
    def crear(self, empleado: Empleado) -> Empleado:
        db_empleado = EmpleadoModel(
            nombre=empleado.nombre,
            email=empleado.email,
            password_hash=empleado.password_hash,
            id_area=empleado.id_area,
            id_cargo=empleado.id_cargo,
        )
        self.db.add(db_empleado)
        self.db.commit()
        self.db.refresh(db_empleado)
        return self._to_entity(db_empleado)
    
    def obtener_por_id(self, id_empleado: int) -> Optional[Empleado]:
        db_empleado = self.db.query(EmpleadoModel).filter(
            EmpleadoModel.id_empleado == id_empleado
        ).first()
        return self._to_entity(db_empleado) if db_empleado else None
    
    def obtener_por_email(self, email: str) -> Optional[Empleado]:
        db_empleado = self.db.query(EmpleadoModel).filter(
            EmpleadoModel.email == email
        ).first()
        return self._to_entity(db_empleado) if db_empleado else None
    
    def existe_email(self, email: str) -> bool:
        return self.db.query(EmpleadoModel).filter(
            EmpleadoModel.email == email
        ).first() is not None
    
    def listar(self, skip: int = 0, limit: int = 100) -> List[Empleado]:
        db_empleados = self.db.query(EmpleadoModel).offset(skip).limit(limit).all()
        return [self._to_entity(e) for e in db_empleados]
    
    def actualizar(self, empleado: Empleado) -> Empleado:
        db_empleado = self.db.query(EmpleadoModel).filter(
            EmpleadoModel.id_empleado == empleado.id_empleado
        ).first()
        if db_empleado:
            db_empleado.nombre = empleado.nombre
            db_empleado.email = empleado.email
            db_empleado.id_area = empleado.id_area
            db_empleado.id_cargo = empleado.id_cargo
            self.db.commit()
            self.db.refresh(db_empleado)
            return self._to_entity(db_empleado)
        return None
    
    def eliminar(self, id_empleado: int) -> bool:
        db_empleado = self.db.query(EmpleadoModel).filter(
            EmpleadoModel.id_empleado == id_empleado
        ).first()
        if db_empleado:
            self.db.delete(db_empleado)
            self.db.commit()
            return True
        return False
    
    def _to_entity(self, model: EmpleadoModel) -> Empleado:
        return Empleado(
            id_empleado=model.id_empleado,
            nombre=model.nombre,
            email=model.email,
            password_hash=model.password_hash,
            id_area=model.id_area,
            id_cargo=model.id_cargo,
        )