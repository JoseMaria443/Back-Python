import io
from datetime import date
from unittest.mock import patch, MagicMock
import pytest
from fastapi.testclient import TestClient

from main import app


class TestArchivoUploadEndpoint:

    @patch("src.infrastructure.adapters.entry.web.archivo.CloudinaryAdapter")
    @patch("src.infrastructure.adapters.entry.web.archivo.ArchivoRepository")
    def test_subir_archivo_exitoso(self, mock_repo, mock_adapter):
        mock_repo_instance = MagicMock()
        mock_repo.return_value = mock_repo_instance
        mock_repo_instance.crear.return_value = MagicMock(
            id_archivo=1,
            doi="doi-001",
            descripcion="Test",
            url_archivo="https://cloudinary.com/test.pdf",
            nombre_original="test.pdf",
            id_elaborador=1,
            fecha_registro=date.today(),
        )
        
        mock_adapter_instance = MagicMock()
        mock_adapter.return_value = mock_adapter_instance
        mock_adapter_instance.subir.return_value = "https://cloudinary.com/test.pdf"
        
        client = TestClient(app)
        response = client.post(
            "/api/archivo/subir",
            files={"file": ("test.pdf", io.BytesIO(b"contenido"), "application/pdf")},
            data={"doi": "doi-001", "descripcion": "Test", "id_elaborador": 1, "fecha_registro": "2025-01-01"},
        )
        
        assert response.status_code == 201

    def test_subir_archivo_extension_no_permitida(self):
        client = TestClient(app)
        response = client.post(
            "/api/archivo/subir",
            files={"file": ("test.txt", io.BytesIO(b"contenido"), "text/plain")},
            data={"doi": "doi-001", "descripcion": "Test", "id_elaborador": 1, "fecha_registro": "2025-01-01"},
        )
        
        assert response.status_code == 400
        assert "Extensión no permitida" in response.json()["detail"]

    def test_subir_archivo_demasiado_grande(self):
        client = TestClient(app)
        contenido_grande = b"x" * (51 * 1024 * 1024)
        response = client.post(
            "/api/archivo/subir",
            files={"file": ("test.pdf", io.BytesIO(contenido_grande), "application/pdf")},
            data={"doi": "doi-001", "descripcion": "Test", "id_elaborador": 1, "fecha_registro": "2025-01-01"},
        )
        
        assert response.status_code == 413