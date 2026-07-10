"""Adaptador de repositorio para Empleado (ORM + SQLAlchemy)."""

from typing import Optional, List
from sqlalchemy.orm import Session
from src.domain.ports.output.empleado import EmpleadoRepositoryPort
from src.domain.entities.empleado import Empleado
from src.infrastructure.adapters.output.persistence.empleado import EmpleadoORM


class EmpleadoRepository(EmpleadoRepositoryPort):
    """Implementación del puerto de repositorio usando SQLAlchemy.
    
    Mapea entre las entidades de dominio y los modelos ORM.
    """

    def __init__(self, session: Session):
        """
        Args:
            session: Sesión de SQLAlchemy
        """
        self.session = session

    def obtener_por_email(self, email: str) -> Optional[Empleado]:
        """Busca un empleado por email usando ORM."""
        empleado_orm = self.session.query(EmpleadoORM).filter(
            EmpleadoORM.email == email
        ).first()
        
        if not empleado_orm:
            return None
        
        return self._orm_a_dominio(empleado_orm)

    def obtener_por_id(self, id_empleado: int) -> Optional[Empleado]:
        """Busca un empleado por ID usando ORM."""
        empleado_orm = self.session.query(EmpleadoORM).filter(
            EmpleadoORM.id_empleado == id_empleado
        ).first()
        
        if not empleado_orm:
            return None
        
        return self._orm_a_dominio(empleado_orm)

    def crear(self, empleado: Empleado) -> Empleado:
        """Crea un nuevo empleado en la BD."""
        empleado_orm = EmpleadoORM(
            nombre=empleado.nombre,
            email=empleado.email,
            password_hash=empleado.password_hash,
            id_area=empleado.id_area,
            id_cargo=empleado.id_cargo,
            activo=empleado.activo,
        )
        
        self.session.add(empleado_orm)
        self.session.commit()
        self.session.refresh(empleado_orm)
        
        return self._orm_a_dominio(empleado_orm)

    def existe_email(self, email: str) -> bool:
        """Verifica si un email ya existe."""
        count = self.session.query(EmpleadoORM).filter(
            EmpleadoORM.email == email
        ).count()
        
        return count > 0

    def listar(self, skip: int = 0, limit: int = 50, nombre: str = None) -> List[Empleado]:
        query = self.session.query(EmpleadoORM)
        if nombre:
            query = query.filter(EmpleadoORM.nombre.ilike(f"%{nombre}%"))
        orms = query.offset(skip).limit(limit).all()
        return [self._orm_a_dominio(orm) for orm in orms]

    def contar(self, nombre: str = None) -> int:
        query = self.session.query(EmpleadoORM)
        if nombre:
            query = query.filter(EmpleadoORM.nombre.ilike(f"%{nombre}%"))
        return query.count()

    def actualizar(self, empleado: Empleado) -> Empleado:
        empleado_orm = self.session.query(EmpleadoORM).filter(
            EmpleadoORM.id_empleado == empleado.id_empleado
        ).first()
        if not empleado_orm:
            return None
        empleado_orm.activo = empleado.activo
        self.session.commit()
        self.session.refresh(empleado_orm)
        return self._orm_a_dominio(empleado_orm)

    def _orm_a_dominio(self, empleado_orm: EmpleadoORM) -> Empleado:
        """Convierte un ORM a entidad de dominio."""
        return Empleado(
            id_empleado=empleado_orm.id_empleado,
            nombre=empleado_orm.nombre,
            email=empleado_orm.email,
            password_hash=empleado_orm.password_hash,
            id_area=empleado_orm.id_area,
            id_cargo=empleado_orm.id_cargo,
            activo=empleado_orm.activo,
        )
