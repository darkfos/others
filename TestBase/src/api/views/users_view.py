from fastapi import APIRouter

from src.api.services.user_service import *
from src.api.schemas.users import *

users_router = APIRouter(prefix="/user", tags=["Users"])


@users_router.get("/{user_id:int}")
def get_user_v(user_id: int):
    return get_user_sr(id_user=user_id)


@users_router.get("/all_users")
def get_all_user_v():
    return get_users_sr()


@users_router.post("/add_user")
def add_user_v(data: AddUser):
    return add_user_sr(data_user=data)


@users_router.delete("/del_user")
def del_user_v(data: DelUser):
    return del_user_sr(data_user=data)