import pytest
from unittest.mock import Mock
from src.application.use_cases.empleado.create_empleado_use_case import CreateEmpleadoUseCase
from src.domain.entities.empleado import Empleado
from src.domain.exceptions import EmailYaExisteException


class TestCreateEmpleadoUseCase:
    def test_crear_empleado_exitoso(self):
        mock_repo = Mock()
        mock_historial_repo = Mock()
        mock_repo.existe_email.return_value = False
        mock_repo.crear.return_value = Empleado(
            id_empleado=1,
            nombre="Juan Pérez",
            email="juan@example.com",
            password_hash="hashed_password",
            id_area=1,
            id_cargo=1,
        )
        
        use_case = CreateEmpleadoUseCase(mock_repo, mock_historial_repo)
        resultado = use_case.ejecutar(
            nombre="Juan Pérez",
            email="juan@example.com",
            password="secret123",
            id_area=1,
            id_cargo=1,
            id_empleado_ejecutor=1,
        )
        
        assert resultado.id_empleado == 1
        assert resultado.nombre == "Juan Pérez"
        assert resultado.email == "juan@example.com"
        mock_repo.existe_email.assert_called_once_with("juan@example.com")
        mock_repo.crear.assert_called_once()
        mock_historial_repo.crear.assert_called_once()

    def test_crear_empleado_email_ya_existe(self):
        mock_repo = Mock()
        mock_historial_repo = Mock()
        mock_repo.existe_email.return_value = True
        
        use_case = CreateEmpleadoUseCase(mock_repo, mock_historial_repo)
        
        with pytest.raises(EmailYaExisteException):
            use_case.ejecutar(
                nombre="Juan Pérez",
                email="juan@example.com",
                password="secret123",
                id_area=1,
                id_cargo=1,
                id_empleado_ejecutor=1,
            )
        
        mock_repo.crear.assert_not_called()
        mock_historial_repo.crear.assert_not_called()
