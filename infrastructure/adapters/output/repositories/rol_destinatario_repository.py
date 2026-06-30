from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.rol_destinatario import RolDestinatario
from src.domain.ports.output.rol_destinatario import RolDestinatarioRepositoryPort
from src.infrastructure.adapters.output.models.rol_destinatario_model import RolDestinatarioModel


class RolDestinatarioRepository(RolDestinatarioRepositoryPort):
    def __init__(self, db: Session):
        self.db = db
    
    def crear(self, rol_destinatario: RolDestinatario) -> RolDestinatario:
        db_rol = RolDestinatarioModel(
            nombre_rol=rol_destinatario.nombre_rol,
            descripcion=rol_destinatario.descripcion,
        )
        self.db.add(db_rol)
        self.db.commit()
        self.db.refresh(db_rol)
        return self._to_entity(db_rol)
    
    def obtener_por_id(self, id_rol_destinatario: int) -> Optional[RolDestinatario]:
        db_rol = self.db.query(RolDestinatarioModel).filter(
            RolDestinatarioModel.id_rol_destinatario == id_rol_destinatario
        ).first()
        return self._to_entity(db_rol) if db_rol else None
    
    def listar(self, skip: int = 0, limit: int = 50) -> List[RolDestinatario]:
        db_roles = self.db.query(RolDestinatarioModel).offset(skip).limit(limit).all()
        return [self._to_entity(r) for r in db_roles]
    
    def actualizar(self, rol_destinatario: RolDestinatario) -> RolDestinatario:
        db_rol = self.db.query(RolDestinatarioModel).filter(
            RolDestinatarioModel.id_rol_destinatario == rol_destinatario.id_rol_destinatario
        ).first()
        if db_rol:
            db_rol.nombre_rol = rol_destinatario.nombre_rol
            db_rol.descripcion = rol_destinatario.descripcion
            self.db.commit()
            self.db.refresh(db_rol)
            return self._to_entity(db_rol)
        return None
    
    def eliminar(self, id_rol_destinatario: int) -> bool:
        db_rol = self.db.query(RolDestinatarioModel).filter(
            RolDestinatarioModel.id_rol_destinatario == id_rol_destinatario
        ).first()
        if db_rol:
            self.db.delete(db_rol)
            self.db.commit()
            return True
        return False
    
    def _to_entity(self, model: RolDestinatarioModel) -> RolDestinatario:
        return RolDestinatario(
            id_rol_destinatario=model.id_rol_destinatario,
            nombre_rol=model.nombre_rol,
            descripcion=model.descripcion,
        )