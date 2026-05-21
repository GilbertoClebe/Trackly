from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
from database import Base
from datetime import date

class Lead(Base) :
    __tablename__ = "leads"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    name: Mapped[str] = mapped_column(String(120))
    last_name: Mapped[str] = mapped_column(String(120))
    number: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(Text)
    address: Mapped[str] = mapped_column()
    birthdate: Mapped[date] = mapped_column()
    occupation: Mapped[str] = mapped_column()
    status: Mapped[str] = mapped_column()
    date_access: Mapped[date] = mapped_column(default=date.today)
    date_update: Mapped[date] = mapped_column(nullable=True)
    
    