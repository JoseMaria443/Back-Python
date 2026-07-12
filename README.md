# Sistema de Gestión de Comunicados

API REST para gestión de comunicados internos con arquitectura hexagonal.

## Requisitos previos

- Python 3.11+ recomendado (Python 3.14 requiere las versiones específicas fijadas en `requirements.txt` para evitar errores de compilación en Windows)
- Docker y Docker Compose (opcional, para PostgreSQL)

## 1. Crear y activar entorno virtual

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac
```bash
python -m venv venv
source venv/bin/activate
```

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 3. Configurar .env

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```bash
DATABASE_URL=postgresql://user:password@localhost:5432/comunicados_db
JWT_SECRET_KEY=tu_secreto_jwt_aqui
JWT_EXPIRATION_HOURS=24
```

Puedes usar `.env.example` como referencia.

## 4. Levantar PostgreSQL

### Opción A: Con Docker Compose
```bash
docker-compose up -d
```

### Opción B: Con instalación local
Asegúrate de tener PostgreSQL instalado y crea la base de datos:
```sql
CREATE DATABASE comunicados_db;
CREATE USER user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE comunicados_db TO user;
```

## 5. Aplicar migraciones

```bash
alembic upgrade head
```

## 6. Encender el servidor

```bash
uvicorn main:app --reload
```

El servidor estará disponible en `http://localhost:8000`.

## 7. Probar

### Swagger UI
Accede a `http://localhost:8000/docs` para ver la documentación interactiva de la API.

### Postman
1. Usa el endpoint `POST /api/empleado/login` con email y password para obtener el token.
2. Copia el token de la respuesta.
3. En otros endpoints, agrega el header: `Authorization: Bearer <token>`.

## 8. Ejecutar tests

```bash
pytest tests/ -v
```

## Documentación de Endpoints

Para el detalle de cada ruta, consulta el archivo `ENDPOINTS.md`.