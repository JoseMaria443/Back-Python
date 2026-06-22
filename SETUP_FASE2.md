# Sistema de Gestión de Comunicados - Guía de Setup

## Setup Inicial

### 1. Crear entorno virtual y instalar dependencias

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar variables de entorno

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env con tus valores
# Particularmente:
# - DATABASE_URL: conexión a PostgreSQL
# - JWT_SECRET_KEY: cambiar a algo seguro
```

### 3. Crear base de datos PostgreSQL

```bash
# Crear BD (usando psql o similar)
createdb comunicados_db

# O con SQL directo:
# CREATE DATABASE comunicados_db;
```

### 4. Ejecutar migraciones (Alembic)

```bash
# Desde la raíz del proyecto
alembic upgrade head
```

### 5. Ejecutar servidor FastAPI

```bash
# Modo desarrollo
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Luego accede a:
# - API: http://localhost:8000
# - Docs (Swagger): http://localhost:8000/docs
# - ReDoc: http://localhost:8000/redoc
```

## Endpoints disponibles en FASE 2

### Login
- **POST** `/api/empleado/login`
  - Body: `{ "email": "...", "password": "..." }`
  - Response: `{ "token": "...", "token_type": "bearer", "id_empleado": ..., "email": "...", "nombre": "..." }`

### Crear Empleado
- **POST** `/api/empleado/crear`
  - Body: `{ "nombre": "...", "email": "...", "password": "...", "id_area": ..., "id_cargo": ... }`
  - Response: `{ "id_empleado": ..., "nombre": "...", "email": "...", "id_area": ..., "id_cargo": ... }`

## Ejemplo de uso (con curl)

```bash
# 1. Crear un empleado de prueba
curl -X POST http://localhost:8000/api/empleado/crear \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan Pérez",
    "email": "juan@ejemplo.com",
    "password": "password123",
    "id_area": 1,
    "id_cargo": 1
  }'

# 2. Login con ese empleado
curl -X POST http://localhost:8000/api/empleado/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "juan@ejemplo.com",
    "password": "password123"
  }'

# 3. Usar el token JWT recibido en headers para otros endpoints (fase siguiente)
# Authorization: Bearer <token>
```

## Estructura de archivos (FASE 2)

```
/src
  /application
    /dtos
      /empleado
        login.py (LoginRequest, LoginResponse)
        create.py (CreateEmpleadoRequest, CreateEmpleadoResponse)
  /domain
    /exceptions
      __init__.py (CredencialesInvalidasException, EmailYaExisteException, etc)
    /ports
      /input
        /empleado
          login_input_port.py (LoginInputPort)
          create_empleado_input_port.py (CreateEmpleadoInputPort)
      /output
        /empleado
          empleado_repository_port.py (EmpleadoRepositoryPort)
  /infrastructure
    /config
      security.py (hash_password, verify_password, crear_token_jwt)
      __init__.py (conexión BD)
    /adapters
      /output
        /repositories
          empleado_repository.py (EmpleadoRepository - implementa puerto)
      /entry
        /web
          empleado.py (routers FastAPI)

main.py (aplicación FastAPI)
alembic/ (migraciones Alembic)
requirements.txt (dependencias)
.env.example (variables de entorno)
```

## Notas de seguridad

- **JWT_SECRET_KEY**: Debe ser una clave fuerte en producción
- **Passwords**: Se hashean con bcrypt (12 rounds) antes de almacenar
- **Login**: No revela si el email existe o si solo el password es incorrecto
- **Endpoint de crear empleado**: Debe protegerse con autenticación/autorización de admin en producción
