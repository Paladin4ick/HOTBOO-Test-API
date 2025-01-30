from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON

from database.base import Base, uuid_pk, str_


class Hotel(Base):
    __tablename__ = "hotels"
    
    id: Mapped[uuid_pk]
    name: Mapped[str_] = mapped_column(comment="Название отеля")
    location: Mapped[str_] = mapped_column(comment="Локация отеля")
    services: Mapped[list] = mapped_column(JSON, comment="Услуги отеля")
    rooms_quantity: Mapped[int] = mapped_column(nullable=False, comment="Кол-во комнат")
    image_id: Mapped[int] = mapped_column(comment="ID изображения")