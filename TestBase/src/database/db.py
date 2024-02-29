from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker

#Подключаемся к БД по адресу, создаем точку входа
engine = create_engine("sqlite:///test.db", echo=True)

# Коннектимся к БД
session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


def connect_to_db():
    """
    Создаеём все таблицы, мета данные, возвращаем объект connect
    :return:
    """

    # Создаём все таблицы хранящиеся в мете
    Base.metadata.create_all(bind=engine)

    with session.begin() as ses:
        return ses