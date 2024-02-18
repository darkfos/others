from dataclasses import dataclass
from typing import Literal


@dataclass
class BaseModel:
    """
    Главный дата класс, необходим для добавления пользователя
    """

    name_customer: str
    surname_customer: str
    price_customer: int
    specialization: Literal["менеджер", "программист", "директор", "дизайнер", "архитектор", "бухгалтер"]
    phone_number: str

    @staticmethod
    def data_attr() -> tuple:
        return "Имя сотрудника", "Фамилия сотрудника", "Заработная плата", "Специализация", "Номер телефона"