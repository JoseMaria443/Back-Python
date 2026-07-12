"""Crear tabla rol_empleado y agregar id_rol a empleado.

Revision ID: 003
Revises: 002
Create Date: 2026-07-12

Cambios:
1. Crear tabla rol_empleado (catálogo de roles de sistema)
2. Agregar columna id_rol a tabla empleado (FK opcional a rol_empleado)
"""
from alembic import op
import sqlalchemy as sa


revision = "003"
down_revision = "002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Crear tabla rol_empleado
    op.create_table(
        'rol_empleado',
        sa.Column('id_rol', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint('id_rol')
    )
    
    # Agregar columna id_rol a empleado
    op.add_column('empleado', sa.Column('id_rol', sa.Integer(), nullable=True))
    op.create_foreign_key(
        'empleado_rol_empleado_fkey',
        'empleado',
        'rol_empleado',
        ['id_rol'],
        ['id_rol']
    )


def downgrade() -> None:
    op.drop_constraint('empleado_rol_empleado_fkey', 'empleado', type_='foreignkey')
    op.drop_column('empleado', 'id_rol')
    op.drop_table('rol_empleado')