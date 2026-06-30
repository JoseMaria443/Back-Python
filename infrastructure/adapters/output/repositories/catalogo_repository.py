from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.catalogo import Catalogo
from src.domain.ports.output.catalogo import CatalogoRepositoryPort
from src.infrastructure.adapters.output.models.catalogo_model import CatalogoModel


class CatalogoRepository(CatalogoRepositoryPort):
    def __init__(self, db: Session):
        self.db = db
    
    def crear(self, catalogo: Catalogo) -> Catalogo:
        db_catalogo = CatalogoModel(
            nombre_catalogo=catalogo.nombre_catalogo,
            id_tipo_catalogo=catalogo.id_tipo_catalogo,
            descripcion=catalogo.descripcion,
        )
        self.db.add(db_catalogo)
        self.db.commit()
        self.db.refresh(db_catalogo)
        return self._to_entity(db_catalogo)
    
    def obtener_por_id(self, id_catalogo: int) -> Optional[Catalogo]:
        db_catalogo = self.db.query(CatalogoModel).filter(
            CatalogoModel.id_catalogo == id_catalogo
        ).first()
        return self._to_entity(db_catalogo) if db_catalogo else None
    
    def listar(self, skip: int = 0, limit: int = 50) -> List[Catalogo]:
        db_catalogos = self.db.query(CatalogoModel).offset(skip).limit(limit).all()
        return [self._to_entity(c) for c in db_catalogos]
    
    def actualizar(self, catalogo: Catalogo) -> Catalogo:
        db_catalogo = self.db.query(CatalogoModel).filter(
            CatalogoModel.id_catalogo == catalogo.id_catalogo
        ).first()
        if db_catalogo:
            db_catalogo.nombre_catalogo = catalogo.nombre_catalogo
            db_catalogo.descripcion = catalogo.descripcion
            self.db.commit()
            self.db.refresh(db_catalogo)
            return self._to_entity(db_catalogo)
        return None
    
    def eliminar(self, id_catalogo: int) -> bool:
        db_catalogo = self.db.query(CatalogoModel).filter(
            CatalogoModel.id_catalogo == id_catalogo
        ).first()
        if db_catalogo:
            self.db.delete(db_catalogo)
            self.db.commit()
            return True
        return False
    
    def _to_entity(self, model: CatalogoModel) -> Catalogo:
        return Catalogo(
            id_catalogo=model.id_catalogo,
            nombre_catalogo=model.nombre_catalogo,
            id_tipo_catalogo=model.id_tipo_catalogo,
            descripcion=model.descripcion,
        )