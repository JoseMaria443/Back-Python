import pytest
from unittest.mock import Mock
from src.application.use_cases.rol_empleado.rol_empleado_use_cases import (
    CreateRolEmpleadoUseCase,
    UpdateRolEmpleadoUseCase,
    DeleteRolEmpleadoUseCase,
    AsignarRolEmpleadoUseCase,
    QuitarRolEmpleadoUseCase,
    ListarRolesEmpleadoUseCase,
    ListRolEmpleadoUseCase,
)
from src.domain.entities.rol_empleado import RolEmpleado
from src.domain.exceptions import RecursoNoEncontradoException, AsociacionYaExisteException, RecursoEnUsoException


class TestCreateRolEmpleadoUseCase:
    def test_crear_rol_empleado_exitoso(self):
        mock_repo = Mock()
        mock_repo.crear.return_value = RolEmpleado(
            id_rol=1,
            descripcion="Administrador",
        )
        
        use_case = CreateRolEmpleadoUseCase(mock_repo)
        resultado = use_case.ejecutar(descripcion="Administrador")
        
        assert resultado.id_rol == 1
        assert resultado.descripcion == "Administrador"
        mock_repo.crear.assert_called_once()


class TestUpdateRolEmpleadoUseCase:
    def test_actualizar_rol_empleado_exitoso(self):
        mock_repo = Mock()
        rol_existente = RolEmpleado(id_rol=1, descripcion="Usuario")
        mock_repo.obtener_por_id.return_value = rol_existente
        mock_repo.actualizar.return_value = RolEmpleado(id_rol=1, descripcion="Administrador")
        
        use_case = UpdateRolEmpleadoUseCase(mock_repo)
        resultado = use_case.ejecutar(id_rol=1, descripcion="Administrador")
        
        assert resultado.descripcion == "Administrador"
        mock_repo.obtener_por_id.assert_called_once_with(1)
        mock_repo.actualizar.assert_called_once()

    def test_actualizar_rol_empleado_no_encontrado(self):
        mock_repo = Mock()
        mock_repo.obtener_por_id.return_value = None
        
        use_case = UpdateRolEmpleadoUseCase(mock_repo)
        
        with pytest.raises(RecursoNoEncontradoException):
            use_case.ejecutar(id_rol=99, descripcion="Administrador")
        
        mock_repo.actualizar.assert_not_called()


class TestDeleteRolEmpleadoUseCase:
    def test_eliminar_rol_empleado_exitoso(self):
        mock_repo = Mock()
        mock_repo.existe_asignado.return_value = False
        mock_repo.eliminar.return_value = True
        
        use_case = DeleteRolEmpleadoUseCase(mock_repo)
        use_case.ejecutar(id_rol=1)
        
        mock_repo.existe_asignado.assert_called_once_with(1)
        mock_repo.eliminar.assert_called_once_with(1)

    def test_eliminar_rol_empleado_asociado(self):
        mock_repo = Mock()
        mock_repo.existe_asignado.return_value = True
        
        use_case = DeleteRolEmpleadoUseCase(mock_repo)
        
        with pytest.raises(RecursoEnUsoException):
            use_case.ejecutar(id_rol=1)
        
        mock_repo.eliminar.assert_not_called()

    def test_eliminar_rol_empleado_no_encontrado(self):
        mock_repo = Mock()
        mock_repo.existe_asignado.return_value = False
        mock_repo.eliminar.return_value = False
        
        use_case = DeleteRolEmpleadoUseCase(mock_repo)
        
        with pytest.raises(RecursoNoEncontradoException):
            use_case.ejecutar(id_rol=99)


class TestAsignarRolEmpleadoUseCase:
    def test_asignar_rol_empleado_exitoso(self):
        mock_rol_repo = Mock()
        mock_empleado_rol_repo = Mock()
        
        rol = RolEmpleado(id_rol=1, descripcion="Administrador")
        mock_rol_repo.obtener_por_id.return_value = rol
        mock_empleado_rol_repo.existe.return_value = False
        
        use_case = AsignarRolEmpleadoUseCase(mock_empleado_rol_repo, mock_rol_repo)
        resultado = use_case.ejecutar(id_empleado=1, id_rol=1)
        
        assert resultado.id_rol == 1
        mock_rol_repo.obtener_por_id.assert_called()
        mock_empleado_rol_repo.existe.assert_called_once_with(1, 1)
        mock_empleado_rol_repo.asignar.assert_called_once_with(1, 1)

    def test_asignar_rol_empleado_rol_no_existe(self):
        mock_rol_repo = Mock()
        mock_empleado_rol_repo = Mock()
        
        mock_rol_repo.obtener_por_id.return_value = None
        
        use_case = AsignarRolEmpleadoUseCase(mock_empleado_rol_repo, mock_rol_repo)
        
        with pytest.raises(RecursoNoEncontradoException):
            use_case.ejecutar(id_empleado=1, id_rol=99)
        
        mock_empleado_rol_repo.asignar.assert_not_called()

    def test_asignar_rol_empleado_ya_asignado(self):
        mock_rol_repo = Mock()
        mock_empleado_rol_repo = Mock()
        
        rol = RolEmpleado(id_rol=1, descripcion="Administrador")
        mock_rol_repo.obtener_por_id.return_value = rol
        mock_empleado_rol_repo.existe.return_value = True
        
        use_case = AsignarRolEmpleadoUseCase(mock_empleado_rol_repo, mock_rol_repo)
        
        with pytest.raises(AsociacionYaExisteException):
            use_case.ejecutar(id_empleado=1, id_rol=1)
        
        mock_empleado_rol_repo.asignar.assert_not_called()


class TestQuitarRolEmpleadoUseCase:
    def test_quitar_rol_empleado_exitoso(self):
        mock_repo = Mock()
        mock_repo.existe.return_value = True
        
        use_case = QuitarRolEmpleadoUseCase(mock_repo)
        use_case.ejecutar(id_empleado=1, id_rol=1)
        
        mock_repo.existe.assert_called_once_with(1, 1)
        mock_repo.quitar.assert_called_once_with(1, 1)

    def test_quitar_rol_empleado_no_encontrado(self):
        mock_repo = Mock()
        mock_repo.existe.return_value = False
        
        use_case = QuitarRolEmpleadoUseCase(mock_repo)
        
        with pytest.raises(RecursoNoEncontradoException):
            use_case.ejecutar(id_empleado=1, id_rol=99)
        
        mock_repo.quitar.assert_not_called()


class TestListarRolesEmpleadoUseCase:
    def test_listar_roles_empleado_vacia(self):
        mock_repo = Mock()
        mock_repo.listar_por_empleado.return_value = []
        
        use_case = ListarRolesEmpleadoUseCase(mock_repo)
        resultado = use_case.ejecutar(id_empleado=1)
        
        assert resultado == []
        mock_repo.listar_por_empleado.assert_called_once_with(1)

    def test_listar_roles_empleado_con_roles(self):
        mock_repo = Mock()
        roles = [
            RolEmpleado(id_rol=1, descripcion="Administrador"),
            RolEmpleado(id_rol=2, descripcion="Supervisor"),
        ]
        mock_repo.listar_por_empleado.return_value = roles
        
        use_case = ListarRolesEmpleadoUseCase(mock_repo)
        resultado = use_case.ejecutar(id_empleado=1)
        
        assert len(resultado) == 2
        assert resultado[0].descripcion == "Administrador"
        assert resultado[1].descripcion == "Supervisor"
        mock_repo.listar_por_empleado.assert_called_once_with(1)


class TestListRolEmpleadoUseCase:
    def test_listar_roles_vacia(self):
        mock_repo = Mock()
        mock_repo.listar.return_value = []
        
        use_case = ListRolEmpleadoUseCase(mock_repo)
        resultado = use_case.ejecutar()
        
        assert resultado == []
        mock_repo.listar.assert_called_once()

    def test_listar_roles_con_roles(self):
        mock_repo = Mock()
        roles = [
            RolEmpleado(id_rol=1, descripcion="Administrador"),
            RolEmpleado(id_rol=2, descripcion="Supervisor"),
        ]
        mock_repo.listar.return_value = roles
        
        use_case = ListRolEmpleadoUseCase(mock_repo)
        resultado = use_case.ejecutar()
        
        assert len(resultado) == 2
        assert resultado[0].descripcion == "Administrador"
        assert resultado[1].descripcion == "Supervisor"
        mock_repo.listar.assert_called_once()