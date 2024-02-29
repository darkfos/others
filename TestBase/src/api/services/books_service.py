#Локальные директивы
from src.database.services.book_service import *
from src.api.schemas import GetBook, ResultBook, AddBook


def get_by_id_sr(id_book: int) -> ResultBook:
    data_result: dict = get_book(id_book=id_book)
    return ResultBook(**data_result)


def get_all_books_sr():
    return get_all_books()


def add_book_sr(data: AddBook) -> bool:
    try:
        add_book(data = data)
        return True
    except Exception as ex:
        return False


def update_book(data: ResultBook) -> ResultBook | dict:
    data_to_response: bool = put_book(data=data)
    if data_to_response:
        return data
    else:
        return {"result": data_to_response}


def delete_book_sr(id_book: int) -> bool:
    result: bool = del_book_by_id(id_book=id_book)
    return result