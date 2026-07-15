from unittest.mock import patch, MagicMock
import pytest

from src.infrastructure.adapters.output.almacenamiento.cloudinary_adapter import CloudinaryAdapter
from src.domain.exceptions.crud_exceptions import ErrorAlmacenamientoException


class TestCloudinaryAdapter:

    @patch("src.infrastructure.adapters.output.almacenamiento.cloudinary_adapter.cloudinary.uploader.upload")
    def test_subir_exitoso(self, mock_upload):
        mock_upload.return_value = {"secure_url": "https://cloudinary.com/test.pdf"}
        
        adapter = CloudinaryAdapter()
        resultado = adapter.subir(b"contenido_test", "test.pdf")
        
        assert resultado == "https://cloudinary.com/test.pdf"
        mock_upload.assert_called_once()

    @patch("src.infrastructure.adapters.output.almacenamiento.cloudinary_adapter.cloudinary.uploader.upload")
    def test_subir_error(self, mock_upload):
        mock_upload.side_effect = Exception("Error de conexión")
        
        adapter = CloudinaryAdapter()
        
        with pytest.raises(ErrorAlmacenamientoException):
            adapter.subir(b"contenido_test", "test.pdf")