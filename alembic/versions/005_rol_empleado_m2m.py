"""Crear tablas rol_empleado y empleado_rol (muchos a muchos).

Revision ID: 005
Revises: 004
Create Date: 2026-07-12

Cambios:
1. Crear tabla rol_empleado (catálogo de roles de sistema)
2. Crear tabla empleado_rol (relación muchos a muchos con fecha_asignacion)
"""
from alembic import op
import sqlalchemy as sa


revision = "005"
down_revision = "004"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'rol_empleado',
        sa.Column('id_rol', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint('id_rol')
    )
    
    op.create_table(
        'empleado_rol',
        sa.Column('id_empleado', sa.Integer(), nullable=False),
        sa.Column('id_rol', sa.Integer(), nullable=False),
        sa.Column('fecha_asignacion', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id_empleado', 'id_rol'),
        sa.ForeignKeyConstraint(['id_empleado'], ['empleado.id_empleado']),
        sa.ForeignKeyConstraint(['id_rol'], ['rol_empleado.id_rol'])
    )


def downgrade() -> None:
    op.drop_table('empleado_rol')
    op.drop_table('rol_empleado')