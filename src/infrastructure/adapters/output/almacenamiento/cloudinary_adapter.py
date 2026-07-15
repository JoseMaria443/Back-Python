import cloudinary.uploader

from src.domain.exceptions.crud_exceptions import ErrorAlmacenamientoException


class CloudinaryAdapter:

    def subir(self, contenido: bytes, nombre_archivo: str) -> str:
        try:
            resultado = cloudinary.uploader.upload(
                contenido,
                public_id=nombre_archivo,
                resource_type="auto",
            )
            return resultado.get("secure_url", "")
        except Exception as e:
            raise ErrorAlmacenamientoException(f"Error al subir archivo a Cloudinary: {str(e)}")