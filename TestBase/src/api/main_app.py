
#Сторонние директивы
from fastapi import FastAPI

import uvicorn

#Локальные директивы
from src.api.views.books_view import book_router
from src.api.views.users_view import users_router


def start_application():
    """
    Запуск API application
    :return:
    """

    application: FastAPI = FastAPI(title="Books api")

    #Добавление роутеров
    application.include_router(book_router)
    application.include_router(users_router)

    return uvicorn.run(application)