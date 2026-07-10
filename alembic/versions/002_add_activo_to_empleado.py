"""Add activo field to empleado table.

Revision ID: 002
Revises: 001
Create Date: 2026-07-10

Cambios:
- Agregar columna 'activo' (boolean, default true) a tabla empleado
"""
from alembic import op
import sqlalchemy as sa


revision = "002"
down_revision = "001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'empleado',
        sa.Column('activo', sa.Boolean(), nullable=False, server_default=sa.text('true'))
    )


def downgrade() -> None:
    op.drop_column('empleado', 'activo')