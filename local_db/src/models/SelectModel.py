from dataclasses import dataclass
from typing import Literal

@dataclass
class SelectModel:
    """
    Дата класс, необходимый для поиска записей по информации
    """

    id_customer: int
    name_customer: str
    surname_customer: str
    price_customer: int
    specialization: Literal["менеджер", "программист", "директор", "дизайнер", "архитектор", "бухгалтер"]
    phone_number: str

    @staticmethod
    def data_attr() -> tuple:
        """
        Статичниый метод вызывается без экземляра класса, необходим для перечисления параметров
        :return:
        """

        return "Ключ", "Имя сотрудника", "Фамилия сотрудника", "Заработная плата", "Специализация", "Номер телефона"