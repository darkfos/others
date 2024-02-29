from src.api.schemas.users import *
from src.database.services.user_service import *
from src.database.models.Users import Users
from src.database.db import connect_to_db


from sqlalchemy import select, insert, update, delete

def get_user_by_id(id_user: int) -> UserSchema:
    session = connect_to_db()
    data: Users = session.execute(select(Users).where(Users.user_id == id_user)).scalar_one()
    data_result: UserSchema = UserSchema(**data.get_dict())
    return data_result


def get_users() -> dict:
    session = connect_to_db()
    data: list = session.execute(select(Users))
    data_result: dict = {id_elem: data_elem for id_elem, data_elem in enumerate(data)}
    return data_result


def add_user(data_user: AddUser) -> dict:
    try:
        session = connect_to_db()
        session.execute(insert(Users).values(**data_user.model_dump()))
        session.commit()
        return {"result": True}
    except Exception as ex:
        return {"result": False}


def del_user(data_user: DelUser) -> dict:
    try:
        session = connect_to_db()
        session.execute(delete(Users).where(Users.user_id == data_user.id))
        return {"result": True}
    except Exception as ex:
        return {"result": False}
