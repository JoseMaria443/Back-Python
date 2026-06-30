from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.emp_cargo import EmpCargo


class EmpCargoRepositoryPort(ABC):
    @abstractmethod
    def crear(self, emp_cargo: EmpCargo) -> EmpCargo:
        pass

    @abstractmethod
    def obtener_por_id(self, id_empleado: int, id_cargo: int) -> Optional[EmpCargo]:
        pass

    @abstractmethod
    def listar(self, skip: int = 0, limit: int = 50) -> List[EmpCargo]:
        pass

    @abstractmethod
    def actualizar(self, emp_cargo: EmpCargo) -> EmpCargo:
        pass

    @abstractmethod
    def eliminar(self, id_empleado: int, id_cargo: int) -> bool:
        pass