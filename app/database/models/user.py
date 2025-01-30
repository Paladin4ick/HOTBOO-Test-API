from database.base import Base, uuid_pk
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[uuid_pk]
    email: Mapped[str] = mapped_column(nullable=False, comment="Почта")
    hashed_password: Mapped[str] = mapped_column(nullable=False, comment="Закеш. пароль")