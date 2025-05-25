"""Файл с исключениями."""

from fastapi import HTTPException, status


class TaskManagementException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class CheckUserException(TaskManagementException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class UnauthedException(TaskManagementException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверная почта или пароль"


class UserIsNotPresentException(TaskManagementException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователя не существует"


class TokenExpiredException(TaskManagementException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен истек"


class TokenAbsentException(TaskManagementException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class IncorrectTokenFormatException(TaskManagementException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"


class NoAccessException(TaskManagementException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Нет доступа"
