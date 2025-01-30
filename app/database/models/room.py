from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, JSON

from database.base import Base, uuid_pk, str_, nmc_10_2

class Room(Base):
    __tablename__ = "rooms"
    
    id: Mapped[uuid_pk]
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"), nullable=False, comment="ID отеля")
    name: Mapped[str_] = mapped_column(nullable=False, comment="Назваие комнаты")
    description: Mapped[str_] = mapped_column(nullable=False, comment="Описание комнаты")
    price: Mapped[nmc_10_2] = mapped_column(nullable=False, comment="Цена за сутки")
    services: Mapped[list] = mapped_column(JSON, nullable=False, comment="Услуги комнаты")
    quantity: Mapped[int] = mapped_column(nullable=False, comment="Кол-во")
    image_id: Mapped[int] = mapped_column(nullable=False, comment="ID картинки")