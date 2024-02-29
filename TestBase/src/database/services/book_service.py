from typing import Any, Generator

from src.database.db import connect_to_db
from src.api.schemas import GetBook, AddBook, ResultBook, UpdateBook
from src.database.models.Books import Books

#Глобальные директивы
from sqlalchemy import select, insert, update, delete
from typing import Any, List

def get_book(id_book: int) -> dict:
    session = connect_to_db()
    result: Books = session.execute(select(Books).where(Books.id_book == id_book)).scalar_one()
    return result.get_dict()


def get_all_books() -> dict:
    session = connect_to_db()
    result = session.execute(select(Books)).scalars().all()
    data_res: dict = {indx: data for indx, data in enumerate(result)}
    return data_res


def add_book(data: AddBook) -> bool:
    try:
        session = connect_to_db()
        stmt = insert(Books).values(**data.model_dump())
        session.execute(stmt)
        session.commit()
        return True
    except Exception:
        return False


def put_book(data: ResultBook) -> bool:
    try:
        session = connect_to_db()
        stmt = session.execute(update(Books).where(Books.id_book == data.id_book).values(**data.model_dump()))
        session.commit()
        return True
    except Exception as ex:
        return False


def del_book_by_id(id_book: int) -> bool:
    try:
        session = connect_to_db()
        stmt = session.execute(delete(Books).where(Books.id_book == id_book))
        session.commit()
        return True
    except Exception as ex:
        return False