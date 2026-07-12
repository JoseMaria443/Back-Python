import pytest
from unittest.mock import Mock
from src.application.use_cases.tipo_catalogo.tipo_catalogo_use_cases import DeleteTipoCatalogoUseCase
from src.application.use_cases.catalogo.catalogo_use_cases import DeleteCatalogoUseCase
from src.application.use_cases.rol_destinatario.rol_destinatario_use_cases import DeleteRolDestinatarioUseCase
from src.application.use_cases.rol_responsable.rol_responsable_use_cases import DeleteRolResponsableUseCase
from src.application.use_cases.rol_empleado.rol_empleado_use_cases import DeleteRolEmpleadoUseCase
from src.domain.exceptions import RecursoNoEncontradoException, RecursoEnUsoException


class TestDeleteTipoCatalogoUseCase:
    def test_eliminar_tipo_catalogo_exitoso(self):
        mock_repo = Mock()
        mock_repo.obtener_por_id.return_value = Mock(id_tipo_catalogo=1, nombre_tipo_catalogo="Tipo 1")
        mock_repo.eliminar.return_value = True

        use_case = DeleteTipoCatalogoUseCase(mock_repo)
        use_case.ejecutar(1)

        mock_repo.eliminar.assert_called_once_with(1)

    def test_eliminar_tipo_catalogo_no_encontrado(self):
        mock_repo = Mock()
        mock_repo.obtener_por_id.return_value = None

        use_case = DeleteTipoCatalogoUseCase(mock_repo)

        with pytest.raises(RecursoNoEncontradoException):
            use_case.ejecutar(999)

    def test_eliminar_tipo_catalogo_en_uso(self):
        mock_repo = Mock()
        mock_repo.obtener_por_id.return_value = Mock(id_tipo_catalogo=1, nombre_tipo_catalogo="Tipo 1")
        mock_repo.eliminar.side_effect = RecursoEnUsoException("No se puede eliminar: el registro está en uso")

        use_case = DeleteTipoCatalogoUseCase(mock_repo)

        with pytest.raises(RecursoEnUsoException):
            use_case.ejecutar(1)


class TestDeleteCatalogoUseCase:
    def test_eliminar_catalogo_exitoso(self):
        mock_repo = Mock()
        mock_repo.obtener_por_id.return_value = Mock(id_catalogo=1, id_tipo_catalogo=1, descripcion="Cat 1")
        mock_repo.eliminar.return_value = True

        use_case = DeleteCatalogoUseCase(mock_repo)
        use_case.ejecutar(1)

        mock_repo.eliminar.assert_called_once_with(1)

    def test_eliminar_catalogo_no_encontrado(self):
        mock_repo = Mock()
        mock_repo.obtener_por_id.return_value = None

        use_case = DeleteCatalogoUseCase(mock_repo)

        with pytest.raises(RecursoNoEncontradoException):
            use_case.ejecutar(999)

    def test_eliminar_catalogo_en_uso(self):
        mock_repo = Mock()
        mock_repo.obtener_por_id.return_value = Mock(id_catalogo=1, id_tipo_catalogo=1, descripcion="Cat 1")
        mock_repo.eliminar.side_effect = RecursoEnUsoException("No se puede eliminar: el registro está en uso")

        use_case = DeleteCatalogoUseCase(mock_repo)

        with pytest.raises(RecursoEnUsoException):
            use_case.ejecutar(1)


class TestDeleteRolDestinatarioUseCase:
    def test_eliminar_rol_destinatario_exitoso(self):
        mock_repo = Mock()
        mock_repo.obtener_por_id.return_value = Mock(id_rol=1, descripcion="Destinatario 1")
        mock_repo.eliminar.return_value = True

        use_case = DeleteRolDestinatarioUseCase(mock_repo)
        use_case.ejecutar(1)

        mock_repo.eliminar.assert_called_once_with(1)

    def test_eliminar_rol_destinatario_no_encontrado(self):
        mock_repo = Mock()
        mock_repo.obtener_por_id.return_value = None

        use_case = DeleteRolDestinatarioUseCase(mock_repo)

        with pytest.raises(RecursoNoEncontradoException):
            use_case.ejecutar(999)

    def test_eliminar_rol_destinatario_en_uso(self):
        mock_repo = Mock()
        mock_repo.obtener_por_id.return_value = Mock(id_rol=1, descripcion="Destinatario 1")
        mock_repo.eliminar.side_effect = RecursoEnUsoException("No se puede eliminar: el registro está en uso")

        use_case = DeleteRolDestinatarioUseCase(mock_repo)

        with pytest.raises(RecursoEnUsoException):
            use_case.ejecutar(1)


class TestDeleteRolResponsableUseCase:
    def test_eliminar_rol_responsable_exitoso(self):
        mock_repo = Mock()
        mock_repo.obtener_por_id.return_value = Mock(id_rol=1, descripcion_rol="Responsable 1")
        mock_repo.eliminar.return_value = True

        use_case = DeleteRolResponsableUseCase(mock_repo)
        use_case.ejecutar(1)

        mock_repo.eliminar.assert_called_once_with(1)

    def test_eliminar_rol_responsable_no_encontrado(self):
        mock_repo = Mock()
        mock_repo.obtener_por_id.return_value = None

        use_case = DeleteRolResponsableUseCase(mock_repo)

        with pytest.raises(RecursoNoEncontradoException):
            use_case.ejecutar(999)

    def test_eliminar_rol_responsable_en_uso(self):
        mock_repo = Mock()
        mock_repo.obtener_por_id.return_value = Mock(id_rol=1, descripcion_rol="Responsable 1")
        mock_repo.eliminar.side_effect = RecursoEnUsoException("No se puede eliminar: el registro está en uso")

        use_case = DeleteRolResponsableUseCase(mock_repo)

        with pytest.raises(RecursoEnUsoException):
            use_case.ejecutar(1)


class TestDeleteRolEmpleadoUseCase:
    def test_eliminar_rol_empleado_exitoso(self):
        mock_repo = Mock()
        mock_repo.existe_asignado.return_value = False
        mock_repo.eliminar.return_value = True

        use_case = DeleteRolEmpleadoUseCase(mock_repo)
        use_case.ejecutar(1)

        mock_repo.eliminar.assert_called_once_with(1)

    def test_eliminar_rol_empleado_no_encontrado(self):
        mock_repo = Mock()
        mock_repo.existe_asignado.return_value = False
        mock_repo.eliminar.return_value = False

        use_case = DeleteRolEmpleadoUseCase(mock_repo)

        with pytest.raises(RecursoNoEncontradoException):
            use_case.ejecutar(999)

    def test_eliminar_rol_empleado_asignado(self):
        mock_repo = Mock()
        mock_repo.existe_asignado.return_value = True

        use_case = DeleteRolEmpleadoUseCase(mock_repo)

        with pytest.raises(RecursoEnUsoException):
            use_case.ejecutar(1)
