from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Computed, ForeignKey, Date

from database.base import Base, uuid_pk, nmc_10_2


class Booking(Base):
    __tablename__ = "bookings"
    
    id: Mapped[uuid_pk]
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[date] = mapped_column(Date, comment="Дата заселения")
    date_to: Mapped[date] = mapped_column(Date, comment="Дата выселения")
    price: Mapped[nmc_10_2] = mapped_column(comment="Цена бронирования")
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"), nullable=False)
    total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"),nullable=False)