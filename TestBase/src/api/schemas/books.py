from pydantic import BaseModel


class GetBook(BaseModel):
    """
    Шаблон для получения книги по id
    """

    id_book: int


class AddBook(BaseModel):
    """
    Шалон для добавления книги
    """

    title_book: str = ""
    price_book: int
    genre_book: str
    author_id: int


class DelBook(BaseModel):
    """
    Шаблон для удаления книги по id
    """

    id_book: int


class UpdateBook(BaseModel):
    """
    Шаблон для обновления книги по id
    """

    id_book: int
    title_book: str
    price_book: int
    genre_book: str
    author_id: int


class ResultBook(BaseModel):
    """
    Шаблон для получения результата
    """

    id_book: int
    title_book: str
    price_book: int
    genre_book: str
    author_id: int