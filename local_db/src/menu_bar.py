import dataclasses

from src.database import Database
from src.models.BaseModel import BaseModel
from src.models.UpdateModel import UpdateModel
from src.models.SelectModel import SelectModel
from src.models.DeleteModel import DeleteModel

import re

def start_application():
    """
    Запуск приложения, точка входа.
    :return:
    """

    print("="*20)
    print("Добро пожаловать в консольный редактор БД - 'Customers'")
    print("="*20)

    menu()
    print("Выберите пункт меню:")
    choice_sel(int(input()))


def menu():
    print("""Пункты меню:
    1. Внести запись
    2. Получить запись
    3. Получить все записи
    4. Обновить информацию
    5. Удалить запись
    """)

def choice_sel(choice: int) -> str:
    """
    Выбор действия от пользователя
    :param choice:
    :return:
    """

    db: Database = Database()

    match choice:
        case 1:
            print("Отлично, вы выбрали пункт 'Внести запись'")
            data_to_add: list = list()

            #Регулярное выражение для поиска номера телефона
            phone_re: re = re.compile(r"8\d{3}\d{3}\d{2}\d{2}")
            for attr in BaseModel.data_attr():
                data_to_add.append(input(attr+": "))

            if phone_re.search(data_to_add[-1]):
                insert_data: BaseModel = BaseModel(*data_to_add)
                db.insert(insert_data)

            else:
                print("Вы ввели не верный номер телефона!")
        case 2:
            print("Отлично, вы выбрали пункт 'Получить запись'")

            lst_data: list = []

            for attr in SelectModel.data_attr():
                attributes = input(attr+": ")
                lst_data.append(attributes)

            data_select: SelectModel = SelectModel(*lst_data)

            result = db.select(data_select=data_select)
            indx = 0
            if result:
                for line in result:
                    print(f"Запись №{indx}: {line}")
                    indx += 1
            else:
                print("К сожалению запись не была найдена")

        case 3:
            print("Отлично, вы выбрали пункт 'Все записи'\n")

            # Получаем все записи
            db.select_all_lines()
        case 4:
            print("Отлично, вы выбрали пункт 'Обновить информацию'\nПожалуйста введите ключ для изменения данных: ")
            key: int = int(input())
            data_to_add: list = list()
            for attr in BaseModel.data_attr():
                data_to_add.append(input(attr+": "))

            update_data: UpdateModel = UpdateModel(*data_to_add)
            db.update(key_find=key, data_update=update_data)
        case 5:
            print("Отлично, вы выбрали пункт 'Удалить запись'")

            data_to_del: list = list()

            re_phone: re = re.compile(r"8\d{3}\d{3}\d{2}\d{2}")

            for attr in BaseModel.data_attr():
                data_to_del.append(input(attr+": "))

            data_to_del: DeleteModel = DeleteModel(*data_to_del)
            if re_phone.search(dataclasses.astuple(data_to_del)[-1]) or dataclasses.astuple(data_to_del)[-1] == "":
                db.delete(data_to_del)
            else:
                print("Неверный номер телефона!")
        case _:
            print("Выбран не существующий формат меню!")


    answer = int(input("Хотите продолжить работу? (1-ДА, 0-НЕТ): "))

    if answer == 1:
        start_application()
    else:
        print("Программа окончила свою работу")