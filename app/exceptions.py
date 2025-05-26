"""Файл с исключениями."""

from fastapi import HTTPException, status


class TaskManagementException(HTTPException):
    """Базовое исключение."""

    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class CheckUserException(TaskManagementException):
    """Исключение если пользователь существует."""

    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class UnauthedException(TaskManagementException):
    """Исключение если неправильная почта или пароль."""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверная почта или пароль"


class UserIsNotPresentException(TaskManagementException):
    """Исключение если юзера нет в бд."""

    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователя не существует"


class TokenExpiredException(TaskManagementException):
    """Исключения если токен истек."""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен истек"


class TokenAbsentException(TaskManagementException):
    """Исключение если токен отсутствует."""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class IncorrectTokenFormatException(TaskManagementException):
    """Исключение неверный формат токена."""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"


class NoAccessException(TaskManagementException):
    """Исключение при отсутствии доступа."""

    status_code = status.HTTP_403_FORBIDDEN
    detail = "Нет доступа"
