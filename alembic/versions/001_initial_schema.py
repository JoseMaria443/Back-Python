"""Initial schema: Fase 1 - Actualizar modelo de datos

Revision ID: 001
Revises: 
Create Date: 2026-06-22

Cambios:
1. Empleado: agregar campos nombre, email, password_hash
2. Comunicado: eliminar IdArchivo
3. Comunicado_adjunto: crear tabla asociativa
4. Tarea: agregar IdEstadoTarea
5. Rol_destinatario: crear catálogo separado
6. Rol_responsable: crear catálogo separado
7. EstadoTarea: crear catálogo específico
8. Estado: crear tabla genérica placeholder
"""
from alembic import op
import sqlalchemy as sa


revision = "001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Crear tabla estado_tarea (catalogo especifico para Tarea)
    op.create_table(
        'estado_tarea',
        sa.Column('id_estado_tarea', sa.Integer(), nullable=False),
        sa.Column('nombre_estado', sa.String(100), nullable=False),
        sa.PrimaryKeyConstraint('id_estado_tarea')
    )

    # Crear tabla estado (catalogo generico)
    op.create_table(
        'estado',
        sa.Column('id_estado', sa.Integer(), nullable=False),
        sa.Column('nombre_estado', sa.String(100), nullable=False),
        sa.PrimaryKeyConstraint('id_estado')
    )

    # Crear tabla rol_destinatario (catalogo separado)
    op.create_table(
        'rol_destinatario',
        sa.Column('id_rol', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint('id_rol')
    )

    # Crear tabla rol_responsable (catalogo separado)
    op.create_table(
        'rol_responsable',
        sa.Column('id_rol', sa.Integer(), nullable=False),
        sa.Column('descripcion_rol', sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint('id_rol')
    )

    # Crear tabla empleado CON nuevos campos
    op.create_table(
        'empleado',
        sa.Column('id_empleado', sa.Integer(), nullable=False),
        sa.Column('nombre', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('password_hash', sa.String(255), nullable=False),
        sa.Column('id_area', sa.Integer(), nullable=False),
        sa.Column('id_cargo', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id_empleado'),
        sa.UniqueConstraint('email')
    )

    # Crear tabla comunicado SIN IdArchivo
    op.create_table(
        'comunicado',
        sa.Column('id_comunicado', sa.Integer(), nullable=False),
        sa.Column('doi', sa.String(255), nullable=False),
        sa.Column('num_comunicado', sa.String(255), nullable=False),
        sa.Column('id_emisor', sa.Integer(), nullable=False),
        sa.Column('fecha_recepcion', sa.Date(), nullable=False),
        sa.Column('id_destinatario', sa.Integer(), nullable=False),
        sa.Column('fecha_registro', sa.Date(), nullable=False),
        sa.Column('id_registro', sa.Integer(), nullable=False),
        sa.Column('id_metodo_recepcion', sa.Integer(), nullable=False),
        sa.Column('tema', sa.String(255), nullable=False),
        sa.Column('observaciones', sa.Text(), nullable=True),
        sa.Column('id_tipo_comunicado', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id_comunicado')
    )

    # Crear tabla comunicado_adjunto (NUEVA - asociativa)
    op.create_table(
        'comunicado_adjunto',
        sa.Column('id_comunicado', sa.Integer(), nullable=False),
        sa.Column('id_archivo', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id_comunicado', 'id_archivo'),
        sa.ForeignKeyConstraint(['id_comunicado'], ['comunicado.id_comunicado']),
        sa.ForeignKeyConstraint(['id_archivo'], ['archivo.id_archivo'])
    )

    # Crear tabla archivo
    op.create_table(
        'archivo',
        sa.Column('id_archivo', sa.Integer(), nullable=False),
        sa.Column('doi', sa.String(255), nullable=False),
        sa.Column('descripcion', sa.Text(), nullable=False),
        sa.Column('url_archivo', sa.String(500), nullable=False),
        sa.Column('nombre_original', sa.String(255), nullable=False),
        sa.Column('id_elaborador', sa.Integer(), nullable=False),
        sa.Column('fecha_registro', sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint('id_archivo'),
        sa.ForeignKeyConstraint(['id_elaborador'], ['empleado.id_empleado'])
    )

    # Crear tabla tarea CON nuevo campo id_estado_tarea
    op.create_table(
        'tarea',
        sa.Column('id_tarea', sa.Integer(), nullable=False),
        sa.Column('id_comunicado', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.Text(), nullable=False),
        sa.Column('fecha_entrega', sa.Date(), nullable=False),
        sa.Column('fecha_registro', sa.Date(), nullable=False),
        sa.Column('id_estado_tarea', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id_tarea'),
        sa.ForeignKeyConstraint(['id_comunicado'], ['comunicado.id_comunicado']),
        sa.ForeignKeyConstraint(['id_estado_tarea'], ['estado_tarea.id_estado_tarea'])
    )

    # Crear tabla tarea_responsable
    op.create_table(
        'tarea_responsable',
        sa.Column('id_tarea', sa.Integer(), nullable=False),
        sa.Column('id_responsable', sa.Integer(), nullable=False),
        sa.Column('id_rol', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id_tarea', 'id_responsable'),
        sa.ForeignKeyConstraint(['id_tarea'], ['tarea.id_tarea']),
        sa.ForeignKeyConstraint(['id_responsable'], ['empleado.id_empleado']),
        sa.ForeignKeyConstraint(['id_rol'], ['rol_responsable.id_rol'])
    )

    # Crear tabla tarea_archivo
    op.create_table(
        'tarea_archivo',
        sa.Column('id_tarea', sa.Integer(), nullable=False),
        sa.Column('id_archivo', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id_tarea', 'id_archivo'),
        sa.ForeignKeyConstraint(['id_tarea'], ['tarea.id_tarea']),
        sa.ForeignKeyConstraint(['id_archivo'], ['archivo.id_archivo'])
    )

    # Crear tabla comunicado_destinatario
    op.create_table(
        'comunicado_destinatario',
        sa.Column('id_comunicado', sa.Integer(), nullable=False),
        sa.Column('id_destinatario', sa.Integer(), nullable=False),
        sa.Column('id_rol_destinatario', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id_comunicado', 'id_destinatario'),
        sa.ForeignKeyConstraint(['id_comunicado'], ['comunicado.id_comunicado']),
        sa.ForeignKeyConstraint(['id_rol_destinatario'], ['rol_destinatario.id_rol'])
    )

    # Crear tabla tipo_catalogo
    op.create_table(
        'tipo_catalogo',
        sa.Column('id_tipo_catalogo', sa.Integer(), nullable=False),
        sa.Column('nombre_tipo_catalogo', sa.String(100), nullable=False),
        sa.PrimaryKeyConstraint('id_tipo_catalogo')
    )

    # Crear tabla catalogo (generico)
    op.create_table(
        'catalogo',
        sa.Column('id_catalogo', sa.Integer(), nullable=False),
        sa.Column('id_tipo_catalogo', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint('id_catalogo'),
        sa.ForeignKeyConstraint(['id_tipo_catalogo'], ['tipo_catalogo.id_tipo_catalogo'])
    )

    # Crear tabla emp_cargo
    op.create_table(
        'emp_cargo',
        sa.Column('id_empleado', sa.Integer(), nullable=False),
        sa.Column('id_cargo', sa.Integer(), nullable=False),
        sa.Column('fecha_inicio', sa.Date(), nullable=False),
        sa.Column('fecha_termina', sa.Date(), nullable=False),
        sa.Column('id_registro_modificacion', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id_empleado', 'id_cargo'),
        sa.ForeignKeyConstraint(['id_empleado'], ['empleado.id_empleado'])
    )


def downgrade() -> None:
    # Eliminar todas las tablas en orden inverso (cuidando FK)
    op.drop_table('emp_cargo')
    op.drop_table('catalogo')
    op.drop_table('tipo_catalogo')
    op.drop_table('comunicado_destinatario')
    op.drop_table('tarea_archivo')
    op.drop_table('tarea_responsable')
    op.drop_table('tarea')
    op.drop_table('archivo')
    op.drop_table('comunicado_adjunto')
    op.drop_table('comunicado')
    op.drop_table('empleado')
    op.drop_table('rol_responsable')
    op.drop_table('rol_destinatario')
    op.drop_table('estado')
    op.drop_table('estado_tarea')
