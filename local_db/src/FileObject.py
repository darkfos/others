
class FileReader:
    """
    Класс для работы с файлами
    """

    @staticmethod
    def read(name_file: str) -> open:
        """
        Статичный метод класса, получаем объкт чтение файла
        :param name_file:
        :return:
        """

        return open(name_file, "r")

    @staticmethod
    def write(name_file: str) -> open:
        """
        Статичный метод класса, получаем объект записи файла
        :param name_file:
        :return:
        """

        return open(name_file, "w")


    @staticmethod
    def write_d(name_file: str) -> open:
        """
        Статичный метод класса, получаем объект дозаписи файла
        :param name_file:
        :return:
        """
        return open(name_file, "a")