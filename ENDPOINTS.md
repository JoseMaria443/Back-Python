# Documentación de Endpoints

## Índice
- [Empleado](#empleado)
- [Estado](#estado)
- [Historial Estado Empleado](#historial-estado-empleado)
- [Rol Empleado](#rol-empleado)

---

## Empleado

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/empleado/login | No | LoginRequest (email: str, password: str) | LoginResponse (token: str, token_type: str, id_empleado: int, email: str, nombre: str) | 200, 401 |
| POST | /api/empleado/crear | Sí | CreateEmpleadoRequest (nombre: str, email: EmailStr, password: str, id_area: int, id_cargo: int) | CreateEmpleadoResponse (id_empleado: int, nombre: str, email: str, id_area: int, id_cargo: int, activo: bool) | 200, 400, 401 |
| GET | /api/empleado/ | Sí | Query params: skip: int, limit: int, nombre: str | ListEmpleadoResponse (items: list[EmpleadoResponse], total: int, skip: int, limit: int) | 200, 401 |
| GET | /api/empleado/{id_empleado} | Sí | Path: id_empleado: int | EmpleadoResponse (id_empleado: int, nombre: str, email: str, id_area: int, id_cargo: int, activo: bool) | 200, 401, 404 |
| PATCH | /api/empleado/{id_empleado}/desactivar | Sí | Path: id_empleado: int | EmpleadoResponse (id_empleado: int, nombre: str, email: str, id_area: int, id_cargo: int, activo: bool) | 200, 401, 404 |
| PATCH | /api/empleado/{id_empleado}/activar | Sí | Path: id_empleado: int | EmpleadoResponse (id_empleado: int, nombre: str, email: str, id_area: int, id_cargo: int, activo: bool) | 200, 401, 404 |
| GET | /api/empleado/{id_empleado}/historial | Sí | Path: id_empleado: int, Query: skip: int, limit: int | ListHistorialEstadoEmpleadoResponse (items: list[HistorialEstadoEmpleadoResponse], total: int, skip: int, limit: int) | 200, 401 |

---

## Estado

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/estado/ | Sí | EstadoRequestDTO (nombre_estado: str) | EstadoResponseDTO (id_estado: int, nombre_estado: str) | 201, 401 |
| GET | /api/estado/{id_estado} | Sí | Path: id_estado: int | EstadoResponseDTO (id_estado: int, nombre_estado: str) | 200, 401, 404 |
| GET | /api/estado/ | Sí | Query params: skip: int, limit: int | ListEstadoResponse (items: list[EstadoResponseDTO], total: int, skip: int, limit: int) | 200, 401 |
| PUT | /api/estado/{id_estado} | Sí | Path: id_estado: int, EstadoRequestDTO (nombre_estado: str) | EstadoResponseDTO (id_estado: int, nombre_estado: str) | 200, 401, 404 |
| DELETE | /api/estado/{id_estado} | Sí | Path: id_estado: int | - | 204, 401, 404 |

---

## Historial Estado Empleado

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| GET | /api/empleado/{id_empleado}/historial | Sí | Path: id_empleado: int, Query: skip: int, limit: int | ListHistorialEstadoEmpleadoResponse (items: list[HistorialEstadoEmpleadoResponse], total: int, skip: int, limit: int) | 200, 401 |

---

## Rol Empleado

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/rol-empleado/ | Sí | CreateRolEmpleadoRequest (descripcion: str) | RolEmpleadoResponse (id_rol: int, descripcion: str) | 201, 401 |
| GET | /api/rol-empleado/ | Sí | Query params: skip: int, limit: int | ListRolEmpleadoResponse (items: list[RolEmpleadoResponse], total: int, skip: int, limit: int) | 200, 401 |
| PUT | /api/rol-empleado/{id_rol} | Sí | Path: id_rol: int, UpdateRolEmpleadoRequest (descripcion: str) | RolEmpleadoResponse (id_rol: int, descripcion: str) | 200, 401, 404 |
| DELETE | /api/rol-empleado/{id_rol} | Sí | Path: id_rol: int | - | 204, 400, 401, 404 |
| POST | /api/rol-empleado/empleado/{id_empleado}/roles | Sí | Path: id_empleado: int, AsignarRolRequest (id_rol: int) | RolEmpleadoResponse (id_rol: int, descripcion: str) | 200, 400, 401, 404 |
| DELETE | /api/rol-empleado/empleado/{id_empleado}/roles/{id_rol} | Sí | Path: id_empleado: int, id_rol: int | - | 204, 401, 404 |
| GET | /api/rol-empleado/empleado/{id_empleado}/roles | Sí | Path: id_empleado: int | ListRolEmpleadoResponse (items: list[RolEmpleadoResponse], total: int, skip: int, limit: int) | 200, 401 |