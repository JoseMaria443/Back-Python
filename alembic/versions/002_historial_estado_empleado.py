"""Crear tabla historial_estado_empleado.

Revision ID: 002
Revises: 001
Create Date: 2026-07-12

Cambios:
1. Crear tabla historial_estado_empleado para auditoría de estados de empleado
"""
from alembic import op
import sqlalchemy as sa


revision = "002"
down_revision = "001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'historial_estado_empleado',
        sa.Column('id_historial', sa.Integer(), nullable=False),
        sa.Column('id_empleado', sa.Integer(), nullable=False),
        sa.Column('accion', sa.String(50), nullable=False),
        sa.Column('id_empleado_ejecutor', sa.Integer(), nullable=False),
        sa.Column('fecha', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id_historial'),
        sa.ForeignKeyConstraint(['id_empleado'], ['empleado.id_empleado']),
        sa.ForeignKeyConstraint(['id_empleado_ejecutor'], ['empleado.id_empleado'])
    )


def downgrade() -> None:
    op.drop_table('historial_estado_empleado')