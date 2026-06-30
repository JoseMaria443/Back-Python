from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.estado import Estado
from src.domain.ports.output.estado import EstadoRepositoryPort
from src.infrastructure.adapters.output.models.estado_model import EstadoModel


class EstadoRepository(EstadoRepositoryPort):
    def __init__(self, db: Session):
        self.db = db
    
    def crear(self, estado: Estado) -> Estado:
        db_estado = EstadoModel(
            nombre_estado=estado.nombre_estado,
            descripcion=estado.descripcion,
        )
        self.db.add(db_estado)
        self.db.commit()
        self.db.refresh(db_estado)
        return self._to_entity(db_estado)
    
    def obtener_por_id(self, id_estado: int) -> Optional[Estado]:
        db_estado = self.db.query(EstadoModel).filter(
            EstadoModel.id_estado == id_estado
        ).first()
        return self._to_entity(db_estado) if db_estado else None
    
    def listar(self, skip: int = 0, limit: int = 50) -> List[Estado]:
        db_estados = self.db.query(EstadoModel).offset(skip).limit(limit).all()
        return [self._to_entity(e) for e in db_estados]
    
    def actualizar(self, estado: Estado) -> Estado:
        db_estado = self.db.query(EstadoModel).filter(
            EstadoModel.id_estado == estado.id_estado
        ).first()
        if db_estado:
            db_estado.nombre_estado = estado.nombre_estado
            db_estado.descripcion = estado.descripcion
            self.db.commit()
            self.db.refresh(db_estado)
            return self._to_entity(db_estado)
        return None
    
    def eliminar(self, id_estado: int) -> bool:
        db_estado = self.db.query(EstadoModel).filter(
            EstadoModel.id_estado == id_estado
        ).first()
        if db_estado:
            self.db.delete(db_estado)
            self.db.commit()
            return True
        return False
    
    def _to_entity(self, model: EstadoModel) -> Estado:
        return Estado(
            id_estado=model.id_estado,
            nombre_estado=model.nombre_estado,
            descripcion=model.descripcion,
        )