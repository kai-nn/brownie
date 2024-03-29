# pidantic
# валидатор, который проверяет данные, ПРИШЕДШИЕ ОТ КЛИЕНТА,
# и взависимости от того соответствуют они следующим соотношениям или нет,
# будет выполняться их передача в FastAPI или они будут отклонены
import pathlib

from pydantic import BaseModel

# Схемы (шаблоны, типы) данных


# валидация данных, пришедших от клиента
class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: str
    is_active: bool

    login: str
    pwd: str


# валидатор транзакций к БД
class UserModel(UserBase):
    id: int

    class Config:
        orm_mode: True


class HomeBase(BaseModel):
    name: str
    description: str


class HomeModel(HomeBase):
    id: int

    class Config:
        orm_mode: True

