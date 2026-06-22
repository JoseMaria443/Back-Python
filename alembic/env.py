"""Alembic configuration for Sistema de Gestión de Comunicados."""

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
import sys
from pathlib import Path

# Agregar src al path para importar modelos
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.infrastructure.adapters.output.persistence.empleado import Base as EmpleadoBase
from src.infrastructure.adapters.output.persistence.comunicado import Base as ComunicadoBase
from src.infrastructure.adapters.output.persistence.tarea import Base as TareaBase
from src.infrastructure.adapters.output.persistence.rol_destinatario import Base as RolDestinatarioBase
from src.infrastructure.adapters.output.persistence.rol_responsable import Base as RolResponsableBase
from src.infrastructure.adapters.output.persistence.estado_tarea import Base as EstadoTareaBase
from src.infrastructure.adapters.output.persistence.estado import Base as EstadoBase

# this is the Alembic Config object, which provides
# the values of the [alembic] section of the setup.cfg file in addition to the
# command line options passed the script's command line arguments we want to
# update with values from this file (as accessed via the `context.config` object)
# for the purposes of 'autogenerate' support. From a programmatic standpoint, the
# various parameters passed to component functions here are imported from the
# .cfg file and parsed.cfg file is in the same directory as a Makefile
# and so we're going to strip the slashes off the paths
# in order to give us relative paths back to where the
# invoke alembic commands are supposed to happen
# from.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = EmpleadoBase.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@localhost:5432/comunicados_db"
    )

    context.configure(
        url=configuration["sqlalchemy.url"],
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@localhost:5432/comunicados_db"
    )

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
