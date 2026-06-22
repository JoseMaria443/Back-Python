# Arquitectura Hexagonal - Estructura del Proyecto

## Visión General

Este proyecto sigue el patrón de **Arquitectura Hexagonal (Ports & Adapters)** para gestionar Comunicados, Tareas, Archivos y Empleados. La estructura separa claramente:

- **Dominio** (Domain): Lógica de negocio pura, independiente de frameworks
- **Aplicación** (Application): Casos de uso, coordinación de dominio
- **Infraestructura** (Infrastructure): Adaptadores (entrada, salida, integraciones)

---

## Estructura de Directorios

```
proyecto-gestion-comunicados/
│
├── src/                              # Código fuente principal
│   ├── __init__.py
│   ├── main.py                       # Punto de entrada de la aplicación
│   │
│   ├── domain/                       # ┌─ CAPA DE DOMINIO
│   │   ├── entities/                 # │  Entidades del negocio
│   │   │   ├── comunicado/           # │  - Comunicado (antes Oficio)
│   │   │   ├── tarea/                # │  - Tarea
│   │   │   ├── archivo/              # │  - Archivo (genérico para evidencias)
│   │   │   ├── empleado/             # │  - Empleado
│   │   │   └── catalogo/             # │  - Catálogos (Estados, Roles, Cargos)
│   │   ├── value_objects/            # │  Value Objects (IDs, Estados, etc)
│   │   ├── ports/                    # │  Interfaces/Puertos (contratos)
│   │   │   ├── input/                # │  - Casos de uso (definiciones)
│   │   │   └── output/               # │  - Repositorios, externos (definiciones)
│   │   └── exceptions/               # │  Excepciones de dominio
│   │                                 # └─
│   │
│   ├── application/                  # ┌─ CAPA DE APLICACIÓN
│   │   ├── use_cases/                # │  Implementación de casos de uso
│   │   │   ├── comunicado/           # │  - CreateComunicado, GetComunicado, etc
│   │   │   ├── tarea/                # │  - CreateTarea, AssignTarea, etc
│   │   │   ├── archivo/              # │  - UploadArchivo, GetArchivo, etc
│   │   │   └── empleado/             # │  - CreateEmpleado, GetEmpleado, etc
│   │   ├── dtos/                     # │  Data Transfer Objects
│   │   │   │                         # │  (para comunicación entre capas)
│   │   │   └── schemas.py            # │  - ComunicadoDTO, TareaDTO, etc
│   │   └── services/                 # │  Servicios transversales
│   │       │                         # │  (notificaciones, auditoría, etc)
│   │       └── .../                  # │
│   │                                 # └─
│   │
│   └── infrastructure/               # ┌─ CAPA DE INFRAESTRUCTURA
│       ├── adapters/                 # │  Adaptadores (implementaciones)
│       │   ├── entry/                # │  ┌─ Adaptadores de ENTRADA
│       │   │   └── web/              # │  │  FastAPI (rutas, esquemas, deps)
│       │   │       ├── routes/       # │  │  - Rutas (endpoints)
│       │   │       ├── schemas/      # │  │  - Esquemas Pydantic
│       │   │       └── dependencies/ # │  │  - Inyección de dependencias
│       │   │                         # │  └─
│       │   ├── output/               # │  ┌─ Adaptadores de SALIDA
│       │   │   ├── persistence/      # │  │  - Configuración BD (MySQL, etc)
│       │   │   │   ├── models.py     # │  │  - Models ORM (SQLAlchemy)
│       │   │   │   └── engine.py     # │  │  - Configuración conexión
│       │   │   └── repositories/     # │  │  - Implementaciones de repositorios
│       │   │       │                 # │  │  (ComunicadoRepository, etc)
│       │   │       └── .../          # │  │
│       │   │                         # │  └─
│       │   └── ai_provider/          # │  ┌─ Adaptador de IA (sin vendor-lock)
│       │       │                     # │  │  Genérico para Gemini/IA futura
│       │       ├── base.py           # │  │  - Interfaz genérica
│       │       ├── gemini/           # │  │  - Implementación Gemini
│       │       └── .../              # │  │  - Otros providers
│       │                             # │  └─
│       └── config/                   # │  ┌─ Configuración
│           ├── settings.py           # │  │  - Configuración general
│           ├── environment.py        # │  │  - Variables de entorno
│           └── .../                  # │  │
│                                     # │  └─
│                                     # └─
│
├── tests/                            # ┌─ PRUEBAS
│   ├── unit/                         # │  ┌─ Tests Unitarios
│   │   ├── domain/                   # │  │  Tests de dominio/entities
│   │   │   └── test_*.py             # │  │
│   │   └── application/              # │  │  Tests de use cases
│   │       └── test_*.py             # │  │
│   │                                 # │  └─
│   └── integration/                  # │  ┌─ Tests de Integración
│       ├── infrastructure/           # │  │  Tests de adaptadores
│       │   └── test_*.py             # │  │
│       └── adapters/                 # │  │  Tests de endpoints, BD, etc
│           └── test_*.py             # │  │
│                                     # │  └─
│                                     # └─
│
├── .env.example                      # Plantilla de variables de entorno
├── .gitignore                        # Archivos a ignorar en git
├── README.md                         # Documentación del proyecto
├── requirements.txt                  # Dependencias (pip)
├── pyproject.toml                    # Configuración proyecto (Poetry/setuptools)
└── docker-compose.yml                # Orquestación (Base de datos, etc)
```

---

## Descripción de Capas

### 1. **DOMAIN (Capa de Dominio)**
Contiene la lógica de negocio pura, independiente de frameworks.

- **`entities/`** → Entidades del negocio (Comunicado, Tarea, Archivo, Empleado, Catálogos)
- **`value_objects/`** → Value Objects (Estados, Roles, etc)
- **`ports/`** → Interfaces/Contratos que definen qué se espera de entrada y salida
  - `input/` → Puertos de entrada (casos de uso que se pueden ejecutar)
  - `output/` → Puertos de salida (qué necesita para funcionar: BD, servicios externos)
- **`exceptions/`** → Excepciones específicas del dominio

### 2. **APPLICATION (Capa de Aplicación)**
Coordina el dominio y ejecuta los casos de uso.

- **`use_cases/`** → Implementación de cada caso de uso
  - `comunicado/` → Crear, actualizar, obtener comunicados
  - `tarea/` → Crear, asignar, actualizar tareas
  - `archivo/` → Subir, descargar, asociar archivos
  - `empleado/` → Crear, actualizar, obtener empleados
- **`dtos/`** → Objetos para transferencia de datos entre capas
- **`services/`** → Servicios transversales (auditoría, notificaciones, etc)

### 3. **INFRASTRUCTURE (Capa de Infraestructura)**
Implementaciones concretas de adaptadores.

#### 3.1 Adaptadores de ENTRADA (`adapters/entry/`)
- **`web/`** → FastAPI
  - `routes/` → Endpoints (GET /comunicados, POST /tareas, etc)
  - `schemas/` → Esquemas Pydantic (validación y serialización)
  - `dependencies/` → Inyección de dependencias (BD, servicios)

#### 3.2 Adaptadores de SALIDA (`adapters/output/`)
- **`persistence/`** → Base de datos
  - Configuración de conexión (MySQL, PostgreSQL, SQLite)
  - Modelos ORM (SQLAlchemy)
- **`repositories/`** → Implementaciones de los puertos de salida
  - `ComunicadoRepository` → Guardar/obtener comunicados
  - `TareaRepository` → Guardar/obtener tareas
  - `ArchivoRepository` → Guardar/obtener archivos
  - `EmpleadoRepository` → Guardar/obtener empleados

#### 3.3 Adaptador de IA (`adapters/ai_provider/`)
Integración genérica (sin vendor lock-in) para:
- Análisis de comunicados (Gemini)
- Extracción de datos (OCR futuro)
- Recomendaciones inteligentes

### 4. **CONFIG (Configuración)**
- **`settings.py`** → Configuración centralizada (BD, API keys, logs)
- **`environment.py`** → Carga de variables de entorno (.env)

### 5. **TESTS (Pruebas)**
- **`unit/`** → Tests unitarios (dominio, aplicación sin dependencias externas)
- **`integration/`** → Tests de integración (adaptadores, BD, API)

---

## Ventajas de esta Arquitectura

✓ **Independencia de frameworks**: Cambiar FastAPI por Flask, MySQL por PostgreSQL sin afectar el dominio  
✓ **Testabilidad**: Mock fácil de puertos/adaptadores  
✓ **Mantenibilidad**: Código organizado, responsabilidades claras  
✓ **Escalabilidad**: Fácil agregar nuevos adaptadores (IA, notificaciones, etc)  
✓ **Sin vendor lock-in**: El adaptador de IA no te ata a Gemini  

---

## Flujo de Datos Típico (Ejemplo: Crear Comunicado)

```
Cliente HTTP
    ↓
[Adaptador de Entrada - FastAPI]
    ↓ schemas.ComunicadoRequest
[Controlador/Endpoint]
    ↓
[Caso de Uso - CreateComunicadoUseCase]
    ↓
[Entidad de Dominio - Comunicado]
    ↓
[Puerto de Salida - ComunicadoRepository (abstracción)]
    ↓
[Adaptador de Salida - ComunicadoRepositoryImpl]
    ↓
[Base de Datos - MySQL]
```

---

## Siguientes Pasos

1. **Implementa el dominio** primero (entidades, value objects, puertos)
2. **Implementa los casos de uso** (servicios de aplicación)
3. **Implementa los adaptadores** (rutas FastAPI, repositorios)
4. **Escriba tests** a medida que desarrollas
5. **Itera y refina** según sea necesario

