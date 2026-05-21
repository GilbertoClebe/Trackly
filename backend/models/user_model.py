from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
from database import Base
from datetime import date

class User(Base) :
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    name: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(120))
    CPF: Mapped[str] = mapped_column(String(11))
    address: Mapped[str] = mapped_column(Text)
    number: Mapped[str] = mapped_column(String(11))
    role: Mapped[str] = mapped_column()
    date_creation: Mapped[date] = mapped_column(default=date.today)
    active: Mapped[bool] = mapped_column(default=True)