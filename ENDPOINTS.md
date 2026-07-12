# Documentación de Endpoints

## Índice
- [Root](#root)
- [Mis módulos](#mis-módulos)
  - [Empleado](#empleado)
  - [Estado](#estado)
  - [Rol Empleado](#rol-empleado)
  - [Emp Cargo](#emp-cargo)
- [Módulos de tu compañero](#módulos-de-tu-compañero)
  - [Comunicado](#comunicado)
  - [Tarea](#tarea)
  - [Archivo](#archivo)
  - [Tipo Catalogo](#tipo-catalogo)
  - [Catalogo](#catalogo)
  - [Rol Destinatario](#rol-destinatario)
  - [Rol Responsable](#rol-responsable)
  - [Estado Tarea](#estado-tarea)

---

## Root

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| GET | / | No | - | {message: str, version: str, status: str} | 200 |
| GET | /health | No | - | {status: str} | 200 |

---

## Mis módulos

### Empleado

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/empleado/login | No | LoginRequest (email: str, password: str) | LoginResponse (token: str, token_type: str, id_empleado: int, email: str, nombre: str) | 200, 401 |
| POST | /api/empleado/crear | Sí | CreateEmpleadoRequest (nombre: str, email: EmailStr, password: str, id_area: int, id_cargo: int) | CreateEmpleadoResponse (id_empleado: int, nombre: str, email: str, id_area: int, id_cargo: int, activo: bool) | 200, 400, 401 |
| GET | /api/empleado/ | Sí | Query params: skip: int, limit: int, nombre: str | ListEmpleadoResponse (items: list[EmpleadoResponse], total: int, skip: int, limit: int) | 200, 401 |
| GET | /api/empleado/{id_empleado} | Sí | Path: id_empleado: int | EmpleadoResponse (id_empleado: int, nombre: str, email: str, id_area: int, id_cargo: int, activo: bool) | 200, 401, 404 |
| PATCH | /api/empleado/{id_empleado}/desactivar | Sí | Path: id_empleado: int | EmpleadoResponse (id_empleado: int, nombre: str, email: str, id_area: int, id_cargo: int, activo: bool) | 200, 401, 404 |
| PATCH | /api/empleado/{id_empleado}/activar | Sí | Path: id_empleado: int | EmpleadoResponse (id_empleado: int, nombre: str, email: str, id_area: int, id_cargo: int, activo: bool) | 200, 401, 404 |
| GET | /api/empleado/{id_empleado}/historial | Sí | Path: id_empleado: int, Query: skip: int, limit: int | ListHistorialEstadoEmpleadoResponse (items: list[HistorialEstadoEmpleadoResponse], total: int, skip: int, limit: int) | 200, 401 |

### Estado

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/estado/ | Sí | EstadoRequestDTO (nombre_estado: str) | EstadoResponseDTO (id_estado: int, nombre_estado: str) | 201, 401 |
| GET | /api/estado/{id_estado} | Sí | Path: id_estado: int | EstadoResponseDTO (id_estado: int, nombre_estado: str) | 200, 401, 404 |
| GET | /api/estado/ | Sí | Query params: skip: int, limit: int | ListEstadoResponse (items: list[EstadoResponseDTO], total: int, skip: int, limit: int) | 200, 401 |
| PUT | /api/estado/{id_estado} | Sí | Path: id_estado: int, EstadoRequestDTO (nombre_estado: str) | EstadoResponseDTO (id_estado: int, nombre_estado: str) | 200, 401, 404 |
| DELETE | /api/estado/{id_estado} | Sí | Path: id_estado: int | - | 204, 401, 404 |

### Rol Empleado

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/rol-empleado/ | Sí | CreateRolEmpleadoRequest (descripcion: str) | RolEmpleadoResponse (id_rol: int, descripcion: str) | 201, 401 |
| GET | /api/rol-empleado/ | Sí | Query params: skip: int, limit: int | ListRolEmpleadoResponse (items: list[RolEmpleadoResponse], total: int, skip: int, limit: int) | 200, 401 |
| PUT | /api/rol-empleado/{id_rol} | Sí | Path: id_rol: int, UpdateRolEmpleadoRequest (descripcion: str) | RolEmpleadoResponse (id_rol: int, descripcion: str) | 200, 401, 404 |
| DELETE | /api/rol-empleado/{id_rol} | Sí | Path: id_rol: int | - | 204, 400, 401, 404 |
| POST | /api/rol-empleado/empleado/{id_empleado}/roles | Sí | Path: id_empleado: int, AsignarRolRequest (id_rol: int) | RolEmpleadoResponse (id_rol: int, descripcion: str) | 200, 400, 401, 404 |
| DELETE | /api/rol-empleado/empleado/{id_empleado}/roles/{id_rol} | Sí | Path: id_empleado: int, id_rol: int | - | 204, 401, 404 |
| GET | /api/rol-empleado/empleado/{id_empleado}/roles | Sí | Path: id_empleado: int | ListRolEmpleadoResponse (items: list[RolEmpleadoResponse], total: int, skip: int, limit: int) | 200, 401 |

### Emp Cargo

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/emp-cargo/ | Sí | AsociarEmpCargoRequest (id_empleado: int, id_cargo: int, fecha_inicio: date, fecha_termina: date, id_registro_modificacion: int) | EmpCargoResponse (id_empleado: int, id_cargo: int, fecha_inicio: date, fecha_termina: date, id_registro_modificacion: int) | 201, 400, 401, 404 |
| DELETE | /api/emp-cargo/{id_empleado}/{id_cargo} | Sí | Path: id_empleado: int, id_cargo: int | - | 204, 401, 404 |

---

## Módulos de tu compañero

### Comunicado

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/comunicado/ | No | CreateComunicadoRequest (doi: str, num_comunicado: str, id_emisor: int, fecha_recepcion: date, id_destinatario: int, fecha_registro: date, id_registro: int, id_metodo_recepcion: int, tema: str, id_tipo_comunicado: int, observaciones: Optional[str]) | ComunicadoResponse (id_comunicado: int, doi: str, num_comunicado: str, id_emisor: int, fecha_recepcion: date, id_destinatario: int, fecha_registro: date, id_registro: int, id_metodo_recepcion: int, tema: str, id_tipo_comunicado: int, observaciones: Optional[str]) | 201, 404 |
| GET | /api/comunicado/{id_comunicado} | No | Path: id_comunicado: int | ComunicadoResponse (id_comunicado: int, doi: str, num_comunicado: str, id_emisor: int, fecha_recepcion: date, id_destinatario: int, fecha_registro: date, id_registro: int, id_metodo_recepcion: int, tema: str, id_tipo_comunicado: int, observaciones: Optional[str]) | 200, 404 |
| GET | /api/comunicado/ | No | Query params: skip: int, limit: int | ListComunicadoResponse (items: list[ComunicadoResponse], total: int, skip: int, limit: int) | 200 |
| PUT | /api/comunicado/{id_comunicado} | No | Path: id_comunicado: int, UpdateComunicadoRequest (doi: str, num_comunicado: str, id_emisor: int, fecha_recepcion: date, id_destinatario: int, fecha_registro: date, id_registro: int, id_metodo_recepcion: int, tema: str, id_tipo_comunicado: int, observaciones: Optional[str]) | ComunicadoResponse (id_comunicado: int, doi: str, num_comunicado: str, id_emisor: int, fecha_recepcion: date, id_destinatario: int, fecha_registro: date, id_registro: int, id_metodo_recepcion: int, tema: str, id_tipo_comunicado: int, observaciones: Optional[str]) | 200, 404 |
| DELETE | /api/comunicado/{id_comunicado} | No | Path: id_comunicado: int | - | 204, 404 |
| POST | /api/comunicado/{id_comunicado}/destinatarios | No | AsociarComunicadoDestinatarioRequest (id_destinatario: int, id_rol_destinatario: int) | ComunicadoDestinatarioResponse (id_comunicado: int, id_destinatario: int, id_rol_destinatario: int) | 201, 400, 404 |
| DELETE | /api/comunicado/{id_comunicado}/destinatarios/{id_destinatario} | No | Path: id_comunicado: int, id_destinatario: int | - | 204, 404 |
| POST | /api/comunicado/{id_comunicado}/adjuntos | No | AsociarComunicadoAdjuntoRequest (id_archivo: int) | ComunicadoAdjuntoResponse (id_comunicado: int, id_archivo: int) | 201, 400, 404 |
| DELETE | /api/comunicado/{id_comunicado}/adjuntos/{id_archivo} | No | Path: id_comunicado: int, id_archivo: int | - | 204, 404 |

### Tarea

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/tarea/ | No | CreateTareaRequest (id_comunicado: int, descripcion: str, fecha_entrega: date, fecha_registro: date, id_estado_tarea: Optional[int]) | TareaResponse (id_tarea: int, id_comunicado: int, descripcion: str, fecha_entrega: date, fecha_registro: date, id_estado_tarea: Optional[int]) | 201, 404 |
| GET | /api/tarea/{id_tarea} | No | Path: id_tarea: int | TareaResponse (id_tarea: int, id_comunicado: int, descripcion: str, fecha_entrega: date, fecha_registro: date, id_estado_tarea: Optional[int]) | 200, 404 |
| GET | /api/tarea/ | No | Query params: skip: int, limit: int | ListTareaResponse (items: list[TareaResponse], total: int, skip: int, limit: int) | 200 |
| PUT | /api/tarea/{id_tarea} | No | Path: id_tarea: int, UpdateTareaRequest (id_comunicado: int, descripcion: str, fecha_entrega: date, fecha_registro: date, id_estado_tarea: Optional[int]) | TareaResponse (id_tarea: int, id_comunicado: int, descripcion: str, fecha_entrega: date, fecha_registro: date, id_estado_tarea: Optional[int]) | 200, 404 |
| DELETE | /api/tarea/{id_tarea} | No | Path: id_tarea: int | - | 204, 404 |
| POST | /api/tarea/{id_tarea}/responsables | No | AsociarTareaResponsableRequest (id_responsable: int, id_rol: int) | TareaResponsableResponse (id_tarea: int, id_responsable: int, id_rol: int) | 201, 400, 404 |
| DELETE | /api/tarea/{id_tarea}/responsables/{id_responsable} | No | Path: id_tarea: int, id_responsable: int | - | 204, 404 |
| POST | /api/tarea/{id_tarea}/archivos | No | AsociarTareaArchivoRequest (id_archivo: int) | TareaArchivoResponse (id_tarea: int, id_archivo: int) | 201, 400, 404 |
| DELETE | /api/tarea/{id_tarea}/archivos/{id_archivo} | No | Path: id_tarea: int, id_archivo: int | - | 204, 404 |

### Archivo

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/archivo/ | No | CreateArchivoRequest (doi: str, descripcion: str, url_archivo: str, nombre_original: str, id_elaborador: int, fecha_registro: date) | ArchivoResponse (id_archivo: int, doi: str, descripcion: str, url_archivo: str, nombre_original: str, id_elaborador: int, fecha_registro: date) | 201, 404 |
| GET | /api/archivo/{id_archivo} | No | Path: id_archivo: int | ArchivoResponse (id_archivo: int, doi: str, descripcion: str, url_archivo: str, nombre_original: str, id_elaborador: int, fecha_registro: date) | 200, 404 |
| GET | /api/archivo/ | No | Query params: skip: int, limit: int | ListArchivoResponse (items: list[ArchivoResponse], total: int, skip: int, limit: int) | 200 |
| PUT | /api/archivo/{id_archivo} | No | Path: id_archivo: int, UpdateArchivoRequest (doi: str, descripcion: str, url_archivo: str, nombre_original: str, id_elaborador: int, fecha_registro: date) | ArchivoResponse (id_archivo: int, doi: str, descripcion: str, url_archivo: str, nombre_original: str, id_elaborador: int, fecha_registro: date) | 200, 404 |
| DELETE | /api/archivo/{id_archivo} | No | Path: id_archivo: int | - | 204, 404 |

### Tipo Catalogo

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/tipo-catalogo/ | Sí | CreateTipoCatalogoRequest (nombre_tipo_catalogo: str) | TipoCatalogoResponse (id_tipo_catalogo: int, nombre_tipo_catalogo: str) | 201, 401 |
| GET | /api/tipo-catalogo/{id_tipo_catalogo} | Sí | Path: id_tipo_catalogo: int | TipoCatalogoResponse (id_tipo_catalogo: int, nombre_tipo_catalogo: str) | 200, 401, 404 |
| GET | /api/tipo-catalogo/ | Sí | Query params: skip: int, limit: int | ListTipoCatalogoResponse (items: list[TipoCatalogoResponse], total: int, skip: int, limit: int) | 200, 401 |
| PUT | /api/tipo-catalogo/{id_tipo_catalogo} | Sí | Path: id_tipo_catalogo: int, UpdateTipoCatalogoRequest (nombre_tipo_catalogo: str) | TipoCatalogoResponse (id_tipo_catalogo: int, nombre_tipo_catalogo: str) | 200, 401, 404 |
| DELETE | /api/tipo-catalogo/{id_tipo_catalogo} | Sí | Path: id_tipo_catalogo: int | - | 204, 401, 404 |

### Catalogo

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/catalogo/ | Sí | CreateCatalogoRequest (id_tipo_catalogo: int, descripcion: str) | CatalogoResponse (id_catalogo: int, id_tipo_catalogo: int, descripcion: str) | 201, 401 |
| GET | /api/catalogo/{id_catalogo} | Sí | Path: id_catalogo: int | CatalogoResponse (id_catalogo: int, id_tipo_catalogo: int, descripcion: str) | 200, 401, 404 |
| GET | /api/catalogo/ | Sí | Query params: skip: int, limit: int | ListCatalogoResponse (items: list[CatalogoResponse], total: int, skip: int, limit: int) | 200, 401 |
| PUT | /api/catalogo/{id_catalogo} | Sí | Path: id_catalogo: int, UpdateCatalogoRequest (id_tipo_catalogo: int, descripcion: str) | CatalogoResponse (id_catalogo: int, id_tipo_catalogo: int, descripcion: str) | 200, 401, 404 |
| DELETE | /api/catalogo/{id_catalogo} | Sí | Path: id_catalogo: int | - | 204, 401, 404 |

### Rol Destinatario

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/rol-destinatario/ | Sí | CreateRolDestinatarioRequest (descripcion: str) | RolDestinatarioResponse (id_rol: int, descripcion: str) | 201, 401 |
| GET | /api/rol-destinatario/{id_rol} | Sí | Path: id_rol: int | RolDestinatarioResponse (id_rol: int, descripcion: str) | 200, 401, 404 |
| GET | /api/rol-destinatario/ | Sí | Query params: skip: int, limit: int | ListRolDestinatarioResponse (items: list[RolDestinatarioResponse], total: int, skip: int, limit: int) | 200, 401 |
| PUT | /api/rol-destinatario/{id_rol} | Sí | Path: id_rol: int, UpdateRolDestinatarioRequest (descripcion: str) | RolDestinatarioResponse (id_rol: int, descripcion: str) | 200, 401, 404 |
| DELETE | /api/rol-destinatario/{id_rol} | Sí | Path: id_rol: int | - | 204, 401, 404 |

### Rol Responsable

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/rol-responsable/ | Sí | CreateRolResponsableRequest (descripcion_rol: str) | RolResponsableResponse (id_rol: int, descripcion_rol: str) | 201, 401 |
| GET | /api/rol-responsable/{id_rol} | Sí | Path: id_rol: int | RolResponsableResponse (id_rol: int, descripcion_rol: str) | 200, 401, 404 |
| GET | /api/rol-responsable/ | Sí | Query params: skip: int, limit: int | ListRolResponsableResponse (items: list[RolResponsableResponse], total: int, skip: int, limit: int) | 200, 401 |
| PUT | /api/rol-responsable/{id_rol} | Sí | Path: id_rol: int, UpdateRolResponsableRequest (descripcion_rol: str) | RolResponsableResponse (id_rol: int, descripcion_rol: str) | 200, 401, 404 |
| DELETE | /api/rol-responsable/{id_rol} | Sí | Path: id_rol: int | - | 204, 401, 404 |

### Estado Tarea

| Método | Ruta | Auth | Request DTO | Response DTO | Status |
|--------|------|------|-------------|--------------|--------|
| POST | /api/estado-tarea/ | No | CreateEstadoTareaRequest (nombre_estado: str) | EstadoTareaResponse (id_estado_tarea: int, nombre_estado: str) | 201, 404 |
| GET | /api/estado-tarea/{id_estado_tarea} | No | Path: id_estado_tarea: int | EstadoTareaResponse (id_estado_tarea: int, nombre_estado: str) | 200, 404 |
| GET | /api/estado-tarea/ | No | Query params: skip: int, limit: int | ListEstadoTareaResponse (items: list[EstadoTareaResponse], total: int, skip: int, limit: int) | 200 |
| PUT | /api/estado-tarea/{id_estado_tarea} | No | Path: id_estado_tarea: int, UpdateEstadoTareaRequest (nombre_estado: str) | EstadoTareaResponse (id_estado_tarea: int, nombre_estado: str) | 200, 404 |
| DELETE | /api/estado-tarea/{id_estado_tarea} | No | Path: id_estado_tarea: int | - | 204, 404 |