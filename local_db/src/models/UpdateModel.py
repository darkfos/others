from dataclasses import dataclass
from typing import Literal


@dataclass
class UpdateModel:
    """
    Дата класс, необходимый для обновления информации
    """

    name_customer: str
    surname_customer: str
    price_customer: int
    specialization: Literal["менеджер", "программист", "директор", "дизайнер", "архитектор", "бухгалтер"]
    phone: str

    def __iter__(self):
        """
        Магический метод, возвращает итератор, необходим для прохода элементов класса
        :return:
        """

        return iter([self.name_customer, self.surname_customer, self.price_customer, self.specialization, self.phone])

    def __len__(self):
        """
        Магический метод, возвращает длину класса, считает количество параметров
        :return:
        """

        return len([self.name_customer, self.surname_customer, self.price_customer, self.specialization, self.phone])