from src.database.services.user_service import *
from src.database.models.Users import Users
from src.database.db import connect_to_db
from src.database.services.user_service import *



def get_user_sr(id_user: int) -> UserSchema:
    data_from_db: UserSchema = get_user_by_id(id_user=id_user)
    return data_from_db


def get_users_sr() -> dict:
    data_from_db: dict = get_users()
    return data_from_db


def add_user_sr(data_user: AddUser) -> dict:
    data_from_db: dict = add_user(data_user=data_user)
    return data_from_db


def del_user_sr(data_user: DelUser) -> dict:
    data_from_db: dict = del_user(data_user=data_user)
    return data_from_db