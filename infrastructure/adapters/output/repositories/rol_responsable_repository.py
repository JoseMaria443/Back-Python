from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.rol_responsable import RolResponsable
from src.domain.ports.output.rol_responsable import RolResponsableRepositoryPort
from src.infrastructure.adapters.output.models.rol_responsable_model import RolResponsableModel


class RolResponsableRepository(RolResponsableRepositoryPort):
    def __init__(self, db: Session):
        self.db = db
    
    def crear(self, rol_responsable: RolResponsable) -> RolResponsable:
        db_rol = RolResponsableModel(
            nombre_rol=rol_responsable.nombre_rol,
            descripcion=rol_responsable.descripcion,
        )
        self.db.add(db_rol)
        self.db.commit()
        self.db.refresh(db_rol)
        return self._to_entity(db_rol)
    
    def obtener_por_id(self, id_rol_responsable: int) -> Optional[RolResponsable]:
        db_rol = self.db.query(RolResponsableModel).filter(
            RolResponsableModel.id_rol_responsable == id_rol_responsable
        ).first()
        return self._to_entity(db_rol) if db_rol else None
    
    def listar(self, skip: int = 0, limit: int = 50) -> List[RolResponsable]:
        db_roles = self.db.query(RolResponsableModel).offset(skip).limit(limit).all()
        return [self._to_entity(r) for r in db_roles]
    
    def actualizar(self, rol_responsable: RolResponsable) -> RolResponsable:
        db_rol = self.db.query(RolResponsableModel).filter(
            RolResponsableModel.id_rol_responsable == rol_responsable.id_rol_responsable
        ).first()
        if db_rol:
            db_rol.nombre_rol = rol_responsable.nombre_rol
            db_rol.descripcion = rol_responsable.descripcion
            self.db.commit()
            self.db.refresh(db_rol)
            return self._to_entity(db_rol)
        return None
    
    def eliminar(self, id_rol_responsable: int) -> bool:
        db_rol = self.db.query(RolResponsableModel).filter(
            RolResponsableModel.id_rol_responsable == id_rol_responsable
        ).first()
        if db_rol:
            self.db.delete(db_rol)
            self.db.commit()
            return True
        return False
    
    def _to_entity(self, model: RolResponsableModel) -> RolResponsable:
        return RolResponsable(
            id_rol_responsable=model.id_rol_responsable,
            nombre_rol=model.nombre_rol,
            descripcion=model.descripcion,
        )