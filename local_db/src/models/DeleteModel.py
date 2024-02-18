from dataclasses import dataclass
from typing import Literal

@dataclass
class DeleteModel:
    """
    Дата класс, необходим для хранения информации при удалении пользователя
    """

    name_customer: str
    surname_customer: str
    price_customer: int
    specializaion: Literal["менеджер", "программист", "директор", "дизайнер", "архитектор", "бухгалтер"]
    phone: str