from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional


@dataclass
class HistorialEstadoEmpleado:
    """Entidad de dominio HistorialEstadoEmpleado.
    
    Registra el historial de cambios de estado de un empleado.
    Cada vez que se crea, activa o desactiva un empleado, se registra
    una entrada en este historial con la fecha y el empleado que ejecutó la acción.
    """
    id_historial: int
    id_empleado: int
    accion: str
    id_empleado_ejecutor: int
    fecha: Optional[datetime] = None

    @staticmethod
    def crear(
        id_empleado: int,
        accion: str,
        id_empleado_ejecutor: int,
    ) -> "HistorialEstadoEmpleado":
        """Factory method para crear una entrada de historial.
        
        La fecha se establece automáticamente al momento de la creación.
        
        Args:
            id_empleado: ID del empleado al que se le cambió el estado
            accion: Acción realizada ("alta", "activar", "desactivar")
            id_empleado_ejecutor: ID del empleado que ejecutó la acción
            
        Returns:
            Instancia de HistorialEstadoEmpleado con fecha establecida
        """
        return HistorialEstadoEmpleado(
            id_historial=0,
            id_empleado=id_empleado,
            accion=accion,
            id_empleado_ejecutor=id_empleado_ejecutor,
            fecha=datetime.now(timezone.utc),
        )
