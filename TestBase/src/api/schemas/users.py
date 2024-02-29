from pydantic import BaseModel


class GetUser(BaseModel):
    """
    Схема для получения пользователя по id
    """

    id: int


class DelUser(BaseModel):
    """
    Схема для удаления пользователя по id
    """

    id: int


class UpdateUser(BaseModel):
    """
    Схема для обновления информации о пользователе
    """

    user_id: int
    name_user: str
    age_user: int
    price_user: int
    specalization: str


class AddUser(BaseModel):
    """
    Схема для добавления пользователя
    """

    name_user: str
    age_user: int
    price_user: int
    specalization: str


class UserSchema(BaseModel):
    """
    Схема пользователя
    """

    user_id: int
    name_user: str
    price_user: int
    specalization: str