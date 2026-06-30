# DIVISIÓN DE TRABAJO - DOS DESARROLLADORES

---

## 👤 DESARROLLADOR 1: Backend Core y Autenticación

### Trabajar en estas carpetas:

```
src/domain/entities/
├── empleado/
├── emp_cargo/
├── tipo_catalogo/
├── catalogo/
├── estado/
├── rol_destinatario/
└── rol_responsable/

src/domain/ports/input/
├── empleado/
├── emp_cargo/
├── tipo_catalogo/
├── catalogo/
├── estado/
├── rol_destinatario/
└── rol_responsable/

src/domain/ports/output/
├── empleado/
├── emp_cargo/
├── tipo_catalogo/
├── catalogo/
├── estado/
├── rol_destinatario/
└── rol_responsable/

src/application/use_cases/
├── empleado/
├── emp_cargo/
├── tipo_catalogo/
├── catalogo/
├── estado/
├── rol_destinatario/
└── rol_responsable/

src/application/dtos/
├── empleado/
├── emp_cargo/
├── tipo_catalogo/
├── catalogo/
├── estado/
├── rol_destinatario/
└── rol_responsable/

infrastructure/
├── config/
│   ├── security.py
│   └── database.py
└── adapters/
    ├── output/
    │   └── repositories/
    └── entry/
        └── main.py
```

### Qué hacer:
- ✅ Configuración de base de datos
- ✅ Sistema de autenticación JWT + bcrypt
- ✅ CRUD de empleado (registro, login, gestión)
- ✅ CRUD de emp_cargo
- ✅ CRUD de tipo_catalogo
- ✅ CRUD de catalogo
- ✅ CRUD de estado
- ✅ CRUD de rol_destinatario
- ✅ CRUD de rol_responsable
- ✅ Middleware de autenticación
- ✅ Configuración de FastAPI

---

## 👤 DESARROLLADOR 2: Módulos de Negocio

### Trabajar en estas carpetas:

```
src/domain/entities/
├── comunicado/
├── comunicado_adjunto/
├── comunicado_destinatario/
├── tarea/
├── tarea_archivo/
├── tarea_responsable/
├── archivo/
└── estado_tarea/

src/domain/ports/input/
├── comunicado/
├── comunicado_adjunto/
├── comunicado_destinatario/
├── tarea/
├── tarea_archivo/
├── tarea_responsable/
├── archivo/
└── estado_tarea/

src/domain/ports/output/
├── comunicado/
├── comunicado_adjunto/
├── comunicado_destinatario/
├── tarea/
├── tarea_archivo/
├── tarea_responsable/
├── archivo/
└── estado_tarea/

src/application/use_cases/
├── comunicado/
├── comunicado_adjunto/
├── comunicado_destinatario/
├── tarea/
├── tarea_archivo/
├── tarea_responsable/
├── archivo/
└── estado_tarea/

src/application/dtos/
├── comunicado/
├── comunicado_adjunto/
├── comunicado_destinatario/
├── tarea/
├── tarea_archivo/
├── tarea_responsable/
├── archivo/
└── estado_tarea/
```

### Qué hacer:
- ✅ CRUD de comunicado
- ✅ CRUD de comunicado_adjunto
- ✅ CRUD de comunicado_destinatario
- ✅ CRUD de tarea
- ✅ CRUD de tarea_archivo
- ✅ CRUD de tarea_responsable
- ✅ CRUD de archivo
- ✅ CRUD de estado_tarea
- ✅ Lógica de negocio de comunicados
- ✅ Lógica de negocio de tareas
- ✅ Endpoints de comunicados y tareas

---

## ⚠️ REGLAS IMPORTANTES

### Desarrollador 1:
- ✅ PUEDE modificar: Sus carpetas listadas arriba
- ❌ NO modificar: Carpetas del Desarrollador 2 (comunicado, tarea, archivo, estado_tarea)

### Desarrollador 2:
- ✅ PUEDE modificar: Sus carpetas listadas arriba
- ❌ NO modificar: Carpetas del Desarrollador 1 (empleado, tipo_catalogo, catalogo, estado, emp_cargo, rol_destinatario, rol_responsable, infrastructure)

### Ambos desarrolladores:
- ✅ PUEDEN modificar: Archivos compartidos de configuración
  - requirements.txt
  - .gitignore
  - README.md
  - src/__init__.py
  - src/domain/__init__.py
  - src/domain/exceptions/ (ambos pueden agregar excepciones)
  - src/domain/value_objects/ (ambos pueden agregar value objects)

---

## 🔄 DEPENDENCIAS

### Desarrollador 2 DEPENDE de Desarrollador 1:
- Entidades: empleado, tipo_catalogo, catalogo, estado, emp_cargo, rol_destinatario, rol_responsable
- Repositorios de estos módulos
- Sistema de autenticación JWT
- Configuración de base de datos

### Desarrollador 1 NO depende de Desarrollador 2:
- Puede trabajar de forma independiente

---

## 📅 ORDEN DE TRABAJO

### Semana 1:
- **Desarrollador 1:** Infraestructura base + autenticación + módulos base
- **Desarrollador 2:** Preparar estructura, definir DTOs y puertos (esperar a Dev 1)

### Semana 2:
- **Desarrollador 1:** Testing y refinamiento
- **Desarrollador 2:** Implementar módulos de comunicados y tareas

### Semana 3:
- **Ambos:** Integración y testing conjunto