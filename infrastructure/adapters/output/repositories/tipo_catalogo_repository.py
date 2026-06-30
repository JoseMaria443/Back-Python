from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.tipo_catalogo import TipoCatalogo
from src.domain.ports.output.tipo_catalogo import TipoCatalogoRepositoryPort
from src.infrastructure.adapters.output.models.tipo_catalogo_model import TipoCatalogoModel


class TipoCatalogoRepository(TipoCatalogoRepositoryPort):
    def __init__(self, db: Session):
        self.db = db
    
    def crear(self, tipo_catalogo: TipoCatalogo) -> TipoCatalogo:
        db_tipo = TipoCatalogoModel(
            nombre_tipo_catalogo=tipo_catalogo.nombre_tipo_catalogo,
        )
        self.db.add(db_tipo)
        self.db.commit()
        self.db.refresh(db_tipo)
        return self._to_entity(db_tipo)
    
    def obtener_por_id(self, id_tipo_catalogo: int) -> Optional[TipoCatalogo]:
        db_tipo = self.db.query(TipoCatalogoModel).filter(
            TipoCatalogoModel.id_tipo_catalogo == id_tipo_catalogo
        ).first()
        return self._to_entity(db_tipo) if db_tipo else None
    
    def listar(self, skip: int = 0, limit: int = 50) -> List[TipoCatalogo]:
        db_tipos = self.db.query(TipoCatalogoModel).offset(skip).limit(limit).all()
        return [self._to_entity(t) for t in db_tipos]
    
    def actualizar(self, tipo_catalogo: TipoCatalogo) -> TipoCatalogo:
        db_tipo = self.db.query(TipoCatalogoModel).filter(
            TipoCatalogoModel.id_tipo_catalogo == tipo_catalogo.id_tipo_catalogo
        ).first()
        if db_tipo:
            db_tipo.nombre_tipo_catalogo = tipo_catalogo.nombre_tipo_catalogo
            self.db.commit()
            self.db.refresh(db_tipo)
            return self._to_entity(db_tipo)
        return None
    
    def eliminar(self, id_tipo_catalogo: int) -> bool:
        db_tipo = self.db.query(TipoCatalogoModel).filter(
            TipoCatalogoModel.id_tipo_catalogo == id_tipo_catalogo
        ).first()
        if db_tipo:
            self.db.delete(db_tipo)
            self.db.commit()
            return True
        return False
    
    def _to_entity(self, model: TipoCatalogoModel) -> TipoCatalogo:
        return TipoCatalogo(
            id_tipo_catalogo=model.id_tipo_catalogo,
            nombre_tipo_catalogo=model.nombre_tipo_catalogo,
        )