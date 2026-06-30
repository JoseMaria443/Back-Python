from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.archivo import Archivo
from src.domain.ports.output.archivo import ArchivoRepositoryPort
from src.infrastructure.adapters.output.persistence.archivo import ArchivoORM


class ArchivoRepository(ArchivoRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def crear(self, archivo: Archivo) -> Archivo:
        orm = ArchivoORM(
            doi=archivo.doi,
            descripcion=archivo.descripcion,
            url_archivo=archivo.url_archivo,
            nombre_original=archivo.nombre_original,
            id_elaborador=archivo.id_elaborador,
            fecha_registro=archivo.fecha_registro,
        )
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def obtener_por_id(self, id_archivo: int) -> Optional[Archivo]:
        orm = self.session.query(ArchivoORM).filter(
            ArchivoORM.id_archivo == id_archivo
        ).first()
        if not orm:
            return None
        return self._orm_a_dominio(orm)

    def listar(self, skip: int, limit: int) -> List[Archivo]:
        orms = self.session.query(ArchivoORM).offset(skip).limit(limit).all()
        return [self._orm_a_dominio(orm) for orm in orms]

    def contar(self) -> int:
        return self.session.query(ArchivoORM).count()

    def actualizar(self, archivo: Archivo) -> Optional[Archivo]:
        orm = self.session.query(ArchivoORM).filter(
            ArchivoORM.id_archivo == archivo.id_archivo
        ).first()
        if not orm:
            return None
        orm.doi = archivo.doi
        orm.descripcion = archivo.descripcion
        orm.url_archivo = archivo.url_archivo
        orm.nombre_original = archivo.nombre_original
        orm.id_elaborador = archivo.id_elaborador
        orm.fecha_registro = archivo.fecha_registro
        self.session.commit()
        self.session.refresh(orm)
        return self._orm_a_dominio(orm)

    def eliminar(self, id_archivo: int) -> bool:
        orm = self.session.query(ArchivoORM).filter(
            ArchivoORM.id_archivo == id_archivo
        ).first()
        if not orm:
            return False
        self.session.delete(orm)
        self.session.commit()
        return True

    def _orm_a_dominio(self, orm: ArchivoORM) -> Archivo:
        return Archivo(
            id_archivo=orm.id_archivo,
            doi=orm.doi,
            descripcion=orm.descripcion,
            url_archivo=orm.url_archivo,
            nombre_original=orm.nombre_original,
            id_elaborador=orm.id_elaborador,
            fecha_registro=orm.fecha_registro,
        )
