# QUÉ DEBE HACER EL DESARROLLADOR 1

---

## 📋 RESUMEN

El Desarrollador 1 es responsable de toda la **infraestructura base del sistema** y los **módulos core** que son fundamentales para que el sistema funcione. Su trabajo es independiente y no depende del Desarrollador 2.

---

## 🎯 MÓDULOS A IMPLEMENTAR (7 módulos)

### 1. EMPLEADO (Autenticación y Usuarios) ⭐ PRIORIDAD ALTA
**Estado actual:** Parcialmente implementado

#### Ya existe:
- ✅ Entidad: `src/domain/entities/empleado/empleado.py`
- ✅ Puerto entrada: `src/domain/ports/input/empleado/login_input_port.py`
- ✅ Puerto entrada: `src/domain/ports/input/empleado/create_empleado_input_port.py`
- ✅ Puerto salida: `src/domain/ports/output/empleado/empleado_repository_port.py`
- ✅ Use Case: `src/application/use_cases/empleado/login_use_case.py`
- ✅ Use Case: `src/application/use_cases/empleado/create_empleado_use_case.py`

#### Falta implementar:
- ❌ DTOs: `src/application/dtos/empleado/` (carpeta vacía o inexistente)
  - `login_dto.py` - DTO para login
  - `create_empleado_dto.py` - DTO para crear empleado
  - `empleado_response_dto.py` - DTO de respuesta
- ❌ Repositorio: `infrastructure/adapters/output/repositories/empleo_repository.py`
  - Implementación SQLAlchemy del repositorio
  - Métodos: crear, obtener_por_id, obtener_por_email, existe_email, listar, actualizar, eliminar
- ❌ Modelo SQLAlchemy: `infrastructure/adapters/output/models/empleado_model.py`
  - Modelo de tabla para SQLAlchemy
- ❌ Endpoints: `infrastructure/adapters/entry/routes/empleado_routes.py`
  - POST /api/empleado/login
  - POST /api/empleado/registro (solo admin)
  - GET /api/empleado/{id}
  - GET /api/empleado/
  - PUT /api/empleado/{id}
  - DELETE /api/empleado/{id}
- ❌ Middleware: `infrastructure/adapters/entry/middleware/auth_middleware.py`
  - Verificación de token JWT
  - Extracción de usuario actual

---

### 2. TIPO_CATALOGO (Tipos de Catálogos) ⭐ PRIORIDAD ALTA
**Estado actual:** Implementado (puede usarse como referencia)

#### Ya existe:
- ✅ Entidad: `src/domain/entities/tipo_catalogo/tipo_catalogo.py`
- ✅ Puerto entrada: `src/domain/ports/input/tipo_catalogo/tipo_catalogo_input_ports.py`
- ✅ Puerto salida: `src/domain/ports/output/tipo_catalogo/__init__.py`
- ✅ Use Cases: `src/application/use_cases/tipo_catalogo/tipo_catalogo_use_cases.py`
  - CreateTipoCatalogoUseCase
  - GetTipoCatalogoUseCase
  - ListTipoCatalogoUseCase
  - UpdateTipoCatalogoUseCase
  - DeleteTipoCatalogoUseCase

#### Falta implementar:
- ❌ DTOs: `src/application/dtos/tipo_catalogo/tipo_catalogo_dtos.py`
- ❌ Repositorio: `infrastructure/adapters/output/repositories/tipo_catalogo_repository.py`
- ❌ Modelo SQLAlchemy: `infrastructure/adapters/output/models/tipo_catalogo_model.py`
- ❌ Endpoints: `infrastructure/adapters/entry/routes/tipo_catalogo_routes.py`
  - POST /api/tipo-catalogo/
  - GET /api/tipo-catalogo/{id}
  - GET /api/tipo-catalogo/
  - PUT /api/tipo-catalogo/{id}
  - DELETE /api/tipo-catalogo/{id}

---

### 3. CATALOGO (Catálogos Generales) ⭐ PRIORIDAD MEDIA
**Estado actual:** Solo estructura de carpetas

#### Falta TODO:
- ❌ Entidad: `src/domain/entities/catalogo/catalogo.py`
- ❌ Puertos entrada: `src/domain/ports/input/catalogo/catalogo_input_ports.py`
- ❌ Puertos salida: `src/domain/ports/output/catalogo/catalogo_repository_port.py`
- ❌ DTOs: `src/application/dtos/catalogo/catalogo_dtos.py`
- ❌ Use Cases: `src/application/use_cases/catalogo/catalogo_use_cases.py`
- ❌ Repositorio: `infrastructure/adapters/output/repositories/catalogo_repository.py`
- ❌ Modelo SQLAlchemy: `infrastructure/adapters/output/models/catalogo_model.py`
- ❌ Endpoints: `infrastructure/adapters/entry/routes/catalogo_routes.py`

---

### 4. ESTADO (Estados Base) ⭐ PRIORIDAD MEDIA
**Estado actual:** Solo estructura de carpetas

#### Falta TODO:
- ❌ Entidad: `src/domain/entities/estado/estado.py`
- ❌ Puertos entrada: `src/domain/ports/input/estado/estado_input_ports.py`
- ❌ Puertos salida: `src/domain/ports/output/estado/estado_repository_port.py`
- ❌ DTOs: `src/application/dtos/estado/estado_dtos.py`
- ❌ Use Cases: `src/application/use_cases/estado/estado_use_cases.py`
- ❌ Repositorio: `infrastructure/adapters/output/repositories/estado_repository.py`
- ❌ Modelo SQLAlchemy: `infrastructure/adapters/output/models/estado_model.py`
- ❌ Endpoints: `infrastructure/adapters/entry/routes/estado_routes.py`

---

### 5. EMP_CARGO (Historial de Cargos) ⭐ PRIORIDAD MEDIA
**Estado actual:** Solo entidad creada

#### Ya existe:
- ✅ Entidad: `src/domain/entities/emp_cargo/emp_cargo.py`

#### Falta TODO:
- ❌ Puertos entrada: `src/domain/ports/input/emp_cargo/emp_cargo_input_ports.py`
- ❌ Puertos salida: `src/domain/ports/output/emp_cargo/emp_cargo_repository_port.py`
- ❌ DTOs: `src/application/dtos/emp_cargo/emp_cargo_dtos.py`
- ❌ Use Cases: `src/application/use_cases/emp_cargo/emp_cargo_use_cases.py`
- ❌ Repositorio: `infrastructure/adapters/output/repositories/emp_cargo_repository.py`
- ❌ Modelo SQLAlchemy: `infrastructure/adapters/output/models/emp_cargo_model.py`
- ❌ Endpoints: `infrastructure/adapters/entry/routes/emp_cargo_routes.py`

---

### 6. ROL_DESTINATARIO (Roles de Destinatario) ⭐ PRIORIDAD MEDIA
**Estado actual:** Solo estructura de carpetas

#### Falta TODO:
- ❌ Entidad: `src/domain/entities/rol_destinatario/rol_destinatario.py`
- ❌ Puertos entrada: `src/domain/ports/input/rol_destinatario/rol_destinatario_input_ports.py`
- ❌ Puertos salida: `src/domain/ports/output/rol_destinatario/rol_destinatario_repository_port.py`
- ❌ DTOs: `src/application/dtos/rol_destinatario/rol_destinatario_dtos.py`
- ❌ Use Cases: `src/application/use_cases/rol_destinatario/rol_destinatario_use_cases.py`
- ❌ Repositorio: `infrastructure/adapters/output/repositories/rol_destinatario_repository.py`
- ❌ Modelo SQLAlchemy: `infrastructure/adapters/output/models/rol_destinatario_model.py`
- ❌ Endpoints: `infrastructure/adapters/entry/routes/rol_destinatario_routes.py`

---

### 7. ROL_RESPONSABLE (Roles de Responsable) ⭐ PRIORIDAD MEDIA
**Estado actual:** Solo estructura de carpetas

#### Falta TODO:
- ❌ Entidad: `src/domain/entities/rol_responsable/rol_responsable.py`
- ❌ Puertos entrada: `src/domain/ports/input/rol_responsable/rol_responsable_input_ports.py`
- ❌ Puertos salida: `src/domain/ports/output/rol_responsable/rol_responsable_repository_port.py`
- ❌ DTOs: `src/application/dtos/rol_responsable/rol_responsable_dtos.py`
- ❌ Use Cases: `src/application/use_cases/rol_responsable/rol_responsable_use_cases.py`
- ❌ Repositorio: `infrastructure/adapters/output/repositories/rol_responsable_repository.py`
- ❌ Modelo SQLAlchemy: `infrastructure/adapters/output/models/rol_responsable_model.py`
- ❌ Endpoints: `infrastructure/adapters/entry/routes/rol_responsable_routes.py`

---

## 🏗️ INFRAESTRUCTURA BASE

### 8. CONFIGURACIÓN ⭐ PRIORIDAD CRÍTICA
**Estado actual:** Parcialmente implementado

#### Ya existe:
- ✅ `infrastructure/config/security.py` (hash_password)

#### Falta implementar:
- ❌ `infrastructure/config/database.py`
  - Configuración de SQLAlchemy
  - Engine, SessionLocal, Base
  - Función get_db()
- ❌ Mejorar `infrastructure/config/security.py`
  - Función hash_password() (ya existe)
  - Función verify_password()
  - Función create_access_token()
  - Función decode_token()
  - Función get_current_user()

### 9. ADAPTADORES (Repositorios y Rutas) ⭐ PRIORIDAD CRÍTICA
**Estado actual:** No existe nada

#### Falta TODO:
- ❌ `infrastructure/adapters/output/repositories/` (carpeta)
  - Todos los repositorios de los 7 módulos
- ❌ `infrastructure/adapters/output/models/` (carpeta)
  - Todos los modelos SQLAlchemy de los 7 módulos
- ❌ `infrastructure/adapters/entry/routes/` (carpeta)
  - Todas las rutas de los 7 módulos
- ❌ `infrastructure/adapters/entry/main.py`
  - Configuración de FastAPI
  - CORS
  - Inclusión de rutas
  - Documentación Swagger

---

## 📊 RESUMEN DE TRABAJO

### Por Prioridad:

#### CRÍTICO (Hacer primero):
1. ✅ Configuración de base de datos (`database.py`)
2. ✅ Mejorar sistema de seguridad (`security.py` completo)
3. ✅ Implementar repositorios base
4. ✅ Implementar modelos SQLAlchemy
5. ✅ Completar módulo EMPLEADO (el más importante)

#### ALTA (Hacer después):
6. ✅ Completar TIPO_CATALOGO (ya tiene estructura)
7. ✅ Implementar CATALOGO
8. ✅ Implementar ESTADO

#### MEDIA (Hacer al final):
9. ✅ Implementar EMP_CARGO
10. ✅ Implementar ROL_DESTINATARIO
11. ✅ Implementar ROL_RESPONSABLE

---

## 🔄 FLUJO DE TRABAJO RECOMENDADO

### Paso 1: Infraestructura Base (Días 1-2)
```
1. Crear infrastructure/config/database.py
2. Completar infrastructure/config/security.py
3. Crear infrastructure/adapters/output/models/ (todos los modelos)
4. Crear infrastructure/adapters/output/repositories/ (todos los repositorios)
```

### Paso 2: Módulo Empleado (Días 3-4)
```
1. Crear DTOs de empleado
2. Implementar repositorio de empleado
3. Crear endpoints de empleado
4. Crear middleware de autenticación
5. Configurar FastAPI en main.py
```

### Paso 3: Módulos Base Restantes (Días 5-7)
```
1. Completar tipo_catalogo (DTOs, repositorio, endpoints)
2. Implementar catalogo (todo)
3. Implementar estado (todo)
4. Implementar emp_cargo (todo)
5. Implementar rol_destinatario (todo)
6. Implementar rol_responsable (todo)
```

---

## 📝 ESTRUCTURA DE ARCHIVOS COMPLETA A CREAR

### Para CADA módulo (7 módulos):
```
módulo/
├── domain/entities/módulo/módulo.py (ya existe en algunos)
├── domain/ports/input/módulo/módulo_input_ports.py
├── domain/ports/output/módulo/módulo_repository_port.py
├── application/dtos/módulo/módulo_dtos.py
├── application/use_cases/módulo/módulo_use_cases.py
├── infrastructure/adapters/output/models/módulo_model.py
├── infrastructure/adapters/output/repositories/módulo_repository.py
└── infrastructure/adapters/entry/routes/módulo_routes.py
```

### Archivos base:
```
infrastructure/
├── config/
│   ├── database.py (NUEVO)
│   └── security.py (COMPLETAR)
└── adapters/
    ├── output/
    │   ├── models/ (carpeta nueva)
    │   └── repositories/ (carpeta nueva)
    └── entry/
        ├── main.py (NUEVO)
        ├── routes/ (carpeta nueva)
        └── middleware/ (carpeta nueva)
```

---

## ⚠️ REGLAS IMPORTANTES

### NO tocar (del Desarrollador 2):
- ❌ `src/domain/entities/comunicado/`
- ❌ `src/domain/entities/comunicado_adjunto/`
- ❌ `src/domain/entities/comunicado_destinatario/`
- ❌ `src/domain/entities/tarea/`
- ❌ `src/domain/entities/tarea_archivo/`
- ❌ `src/domain/entities/tarea_responsable/`
- ❌ `src/domain/entities/archivo/`
- ❌ `src/domain/entities/estado_tarea/`
- ❌ Todas las carpetas de ports, use_cases y dtos de esos módulos

### SÍ tocar:
- ✅ `src/domain/entities/empleado/`
- ✅ `src/domain/entities/emp_cargo/`
- ✅ `src/domain/entities/tipo_catalogo/`
- ✅ `src/domain/entities/catalogo/`
- ✅ `src/domain/entities/estado/`
- ✅ `src/domain/entities/rol_destinatario/`
- ✅ `src/domain/entities/rol_responsable/`
- ✅ Todas las carpetas de ports, use_cases y dtos de esos módulos
- ✅ Toda la carpeta `infrastructure/`

---

## 🎯 OBJETIVO FINAL

Al finalizar, el Desarrollador 1 debe tener:
1. ✅ Sistema de autenticación completo (JWT)
2. ✅ Base de datos configurada y migraciones listas
3. ✅ 7 módulos CRUD completamente funcionales
4. ✅ API REST funcionando con FastAPI
5. ✅ Documentación Swagger disponible
6. ✅ Middleware de autenticación funcionando

**El sistema debe estar listo para que el Desarrollador 2 pueda usarlo como base para sus módulos de negocio.**