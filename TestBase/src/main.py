from src.database.db import connect_to_db

#Подключаем таблицы
from src.database.models.Users import Users
from src.database.models.Books import Books

from src.api.main_app import start_application

if __name__ == "__main__":
    connect_to_db()
    start_application()