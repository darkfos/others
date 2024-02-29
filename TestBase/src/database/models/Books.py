from src.database.db import Base

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Books(Base):
    __tablename__ = "Books"

    id_book: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title_book: Mapped[str] = mapped_column(String(150))
    price_book: Mapped[int] = mapped_column(Integer)
    genre_book: Mapped[str] = mapped_column(String(400))
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("Users.user_id", ondelete="CASCADE"))
    user: Mapped[int] = relationship("Users")

    def __repr__(self):
        return "<Books: id_book: {}, title_book: {}, price_book: {}, genre_book: {}, author_id: {}>".format(
            self.id_book, self.title_book, self.price_book, self.genre_book, self.author_id
        )

    def get_dict(self):
        return {"id_book": self.id_book, "title_book": self.title_book,
                "price_book": self.price_book, "genre_book": self.genre_book,
                "author_id": self.author_id}
