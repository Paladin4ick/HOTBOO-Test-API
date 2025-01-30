import datetime
import uuid
import enum
from decimal import Decimal
from typing import Annotated
from sqlalchemy import DateTime, Integer, String, Numeric, Enum
from sqlalchemy.orm import DeclarativeBase, mapped_column, registry

uuid_pk = Annotated[int, mapped_column(Integer, primary_key=True, default=uuid.uuid4)]
str_ = Annotated[str, mapped_column(String, nullable=False)]
nmc_10_2 = Annotated[Decimal, mapped_column(Numeric(precision=10, scale=2), nullable=False)]

class Base(DeclarativeBase):
    pass