"""Excepciones del dominio."""


class DomainException(Exception):
    """Clase base para todas las excepciones del dominio."""
    pass


class CredencialesInvalidasException(DomainException):
    """Se lanza cuando las credenciales (email/password) son inválidas."""
    pass


class EmailYaExisteException(DomainException):
    """Se lanza cuando se intenta crear un empleado con un email ya registrado."""
    pass


class EmpleadoNoEncontradoException(DomainException):
    """Se lanza cuando no se encuentra un empleado."""
    pass


from .crud_exceptions import RecursoNoEncontradoException, AsociacionYaExisteException

__all__ = [
    "DomainException",
    "CredencialesInvalidasException",
    "EmailYaExisteException",
    "EmpleadoNoEncontradoException",
    "RecursoNoEncontradoException",
    "AsociacionYaExisteException",
]
