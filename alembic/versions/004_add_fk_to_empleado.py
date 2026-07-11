"""Add foreign keys to empleado table.

Revision ID: 004
Revises: 003
Create Date: 2026-07-10

Cambios:
- Agregar FK empleado.id_area -> catalogo.id_catalogo
- Agregar FK empleado.id_cargo -> catalogo.id_catalogo
"""
from alembic import op
import sqlalchemy as sa


revision = "004"
down_revision = "003"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_foreign_key(
        'fk_empleado_id_area',
        'empleado',
        'catalogo',
        ['id_area'],
        ['id_catalogo']
    )
    op.create_foreign_key(
        'fk_empleado_id_cargo',
        'empleado',
        'catalogo',
        ['id_cargo'],
        ['id_catalogo']
    )


def downgrade() -> None:
    op.drop_constraint('fk_empleado_id_area', 'empleado', type_='foreignkey')
    op.drop_constraint('fk_empleado_id_cargo', 'empleado', type_='foreignkey')