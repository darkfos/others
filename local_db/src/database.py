import typing
import dataclasses
import random

from src.models.BaseModel import BaseModel
from src.models.UpdateModel import UpdateModel
from src.FileObject import FileReader
from src.models.SelectModel import SelectModel
from src.models.DeleteModel import DeleteModel


class Database:

    def __init__(self):
        """
        Инициаоизация данных, хранение БД, подключением
        """

        self.db_name: str = "list_customers.txt"
        self.db_name_pr: str = "primary_key.txt"
        self.connect = open

    def select_all_lines(self) -> typing.Union[str, int]:
        """
        Генератор, возвращаем значение, запоминаем состояние
        :return:
        """

        file = FileReader.read(self.db_name)
        indx: int = 0
        for line in file.readlines():
            print("Запись №{0}: ".format(indx) + line)
            indx += 1

    def insert(self, data_add: BaseModel) -> bool:
        """
        Метод, для добавления значений
        :return:
        """

        file = FileReader.write_d(self.db_name)

        #Генерация первичного ключа
        random_pr: int = random.randint(1, 10000000000)
        #Получаем все первичные ключи, которые были
        all_pr_key: list = list()

        file_read: open = FileReader.read(self.db_name_pr)
        for line in file_read.readlines():
            all_pr_key.append(int(line))

        if str(random_pr) not in all_pr_key:
            wr_in_file: open = FileReader.write_d(self.db_name_pr)

            wr_in_file.write(str(random_pr)+"\n")

            line_to_add: str = ",".join(list(dataclasses.asdict(data_add).values()))
            file.write("\n" + str(random_pr) + "," + line_to_add)
            wr_in_file.close()
        else:
            file_read.close()
            return False

        return True

    def select(self, data_select: SelectModel) -> bool | list:
        """
        Метод, для вывода записей по фильтру
        :return:
        """

        #Открываем файл
        file: open = FileReader.read(self.db_name)
        answer_data: list = []

        answer_line = ""
        for line in file.readlines():
            for data_s in dataclasses.astuple(data_select):
                if data_s.strip() not in ("", "\n"):
                    answer_line += data_s + ","

            if answer_line in line:
                answer_data.append(line)
            answer_line = ""


        if answer_data: return answer_data
        return False

    def update(self, key_find: int, data_update: UpdateModel) -> bool:
        """
        Метод, для обновления информации по параметрам
        :param data_find:
        :param data_update:
        :return:
        """

        file = FileReader.read(self.db_name)

        all_lines: list = list()

        for line in file.readlines():
            if line != "":
                data_str: list = line.split(",")
                if data_str[0].isdigit() and int(data_str[0]) == key_find:
                    for indx, data in enumerate(data_update):
                        if data != "":
                            data_str[indx+1] = data
                    all_lines.append(",".join(data_str))
                else:
                    all_lines.append(",".join(data_str))
                    continue
            else:
                continue

        self.write_data("\n".join(all_lines))

    def delete(self, data_del: DeleteModel) -> bool:
        """
        Метод для удаления записей в файле БД по аргументам
        :param args:
        :return:
        """

        try:
            file_r: open = FileReader.read(self.db_name)
            all_lines: list = list()
            data_to_del_str: str = str()
            for param in dataclasses.astuple(data_del):
                if param not in ("", "\n"):
                    data_to_del_str += param + ","
            for line in file_r.readlines():
                all_lines.append(line)
                if data_to_del_str in line:
                    del all_lines[all_lines.index(line)]

            #Записываем обратно данные
            file_w: open = FileReader.write(self.db_name)
            file_w.writelines(all_lines)
            return True

        except Exception as ex:
            return False

    def write_data(self, data: str) -> bool:
        """
        Метод для записи данных
        :param self:
        :param data:
        :return:
        """

        try:
            file: FileReader = FileReader.write(self.db_name)

            file.writelines(data)

            return True
        except Exception as ex:
            return False
