from dataclasses import dataclass


@dataclass
class RolDestinatario:
    """Entidad de dominio Rol_Destinatario.
    
    Catálogo separado para roles de destinatarios en Comunicado_Destinatario.
    Ejemplo: Principal, Con copia, Informativo.
    """
    id_rol: int
    descripcion: str
