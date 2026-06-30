from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infrastructure.config.database import get_db
from src.infrastructure.config.security import hash_password, verify_password, create_access_token
from src.application.use_cases.empleado.create_empleado_use_case import CreateEmpleadoUseCase
from src.application.use_cases.empleado.login_use_case import LoginUseCase
from src.infrastructure.adapters.output.repositories.empleado_repository import EmpleadoRepository
from src.application.dtos.empleado.login_dto import LoginRequestDTO, LoginResponseDTO
from src.application.dtos.empleado.create_empleado_dto import CreateEmpleadoRequestDTO, CreateEmpleadoResponseDTO
from src.application.dtos.empleado.empleado_response_dto import EmpleadoResponseDTO

router = APIRouter(prefix="/api/empleado", tags=["empleado"])


@router.post("/login", response_model=LoginResponseDTO)
def login(login_data: LoginRequestDTO, db: Session = Depends(get_db)):
    repository = EmpleadoRepository(db)
    use_case = LoginUseCase(repository)
    
    try:
        resultado = use_case.ejecutar(login_data.email, login_data.password)
        access_token = create_access_token(data={
            "sub": resultado.email,
            "id_empleado": resultado.id_empleado,
            "nombre": resultado.nombre,
        })
        return LoginResponseDTO(
            access_token=access_token,
            id_empleado=resultado.id_empleado,
            nombre=resultado.nombre,
            email=resultado.email,
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))


@router.post("/registro", response_model=CreateEmpleadoResponseDTO, status_code=status.HTTP_201_CREATED)
def registrar(request: CreateEmpleadoRequestDTO, db: Session = Depends(get_db)):
    repository = EmpleadoRepository(db)
    use_case = CreateEmpleadoUseCase(repository)
    
    try:
        resultado = use_case.ejecutar(
            nombre=request.nombre,
            email=request.email,
            password=request.password,
            id_area=request.id_area,
            id_cargo=request.id_cargo,
        )
        return CreateEmpleadoResponseDTO(
            id_empleado=resultado.id_empleado,
            nombre=resultado.nombre,
            email=resultado.email,
            id_area=resultado.id_area,
            id_cargo=resultado.id_cargo,
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{id_empleado}", response_model=EmpleadoResponseDTO)
def obtener_empleado(id_empleado: int, db: Session = Depends(get_db)):
    repository = EmpleadoRepository(db)
    empleado = repository.obtener_por_id(id_empleado)
    if not empleado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Empleado no encontrado")
    return EmpleadoResponseDTO(
        id_empleado=empleado.id_empleado,
        nombre=empleado.nombre,
        email=empleado.email,
        id_area=empleado.id_area,
        id_cargo=empleado.id_cargo,
    )


@router.get("/", response_model=list[EmpleadoResponseDTO])
def listar_empleados(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    repository = EmpleadoRepository(db)
    empleados = repository.listar(skip=skip, limit=limit)
    return [
        EmpleadoResponseDTO(
            id_empleado=e.id_empleado,
            nombre=e.nombre,
            email=e.email,
            id_area=e.id_area,
            id_cargo=e.id_cargo,
        )
        for e in empleados
    ]