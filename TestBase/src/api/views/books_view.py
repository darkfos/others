#Глобальные директивы
from fastapi import APIRouter

#Локальные директивы
from src.api.schemas import GetBook, ResultBook, AddBook, UpdateBook
from src.api.services.books_service import get_by_id_sr, get_all_books_sr, add_book_sr, update_book, delete_book_sr
from typing import Dict


book_router: APIRouter = APIRouter(prefix="/book", tags=["Books"])

@book_router.get("/get/{id_book:int}")
def get_book(id_book: int) -> ResultBook:
    data_response: ResultBook = get_by_id_sr(id_book=id_book)
    return data_response


@book_router.get("/get_all")
def get_all_books():
    return get_all_books_sr()


@book_router.post("/post-book")
def post_book(data_to_add: AddBook) -> Dict[str, bool]:
    result = add_book_sr(data=data_to_add)
    return {"result": result}


@book_router.put("/put-book")
def put_book(data_update: ResultBook):
    return update_book(data=data_update)


@book_router.delete("/del-book/{id_book:int}}")
def del_book(id_book: int) -> dict:
    result: bool = delete_book_sr(id_book)

    if result:
        return {"succes": result}
    return {"success": result}