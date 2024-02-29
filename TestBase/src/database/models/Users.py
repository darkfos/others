from src.database.db import Base

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Users(Base):
    __tablename__ = "Users"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name_user: Mapped[str] = mapped_column(String(250))
    age_user: Mapped[int] = mapped_column(Integer)
    price_user: Mapped[int] = mapped_column(Integer)
    specalization: Mapped[str] = mapped_column(String(350))

    def __repr__(self):
        return "<Users: user_id: {}, name_user: {}, age_user: {}, price_user: {}, specalization: {}>".format(
            self.user_id, self.name_user, self.age_user, self.price_user, self.specalization
        )

    def get_dict(self):
        return {"user_id": self.user_id, "name_user": self.name_user,
                "age_user": self.age_user, "price_user": self.price_user,
                "specalization": self.specalization}