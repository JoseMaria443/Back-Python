"""Base declarativa compartida para todos los modelos ORM.

Este archivo define el único Base que deben usar todos los modelos ORM.
Centralizar el Base permite que SQLAlchemy maneje correctamente las relaciones
ForeignKey entre modelos definidos en archivos distintos.
"""

from sqlalchemy.orm import declarative_base

# Único Base compartido para todos los modelos ORM
Base = declarative_base()
