from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
from database import Base
from datetime import date

class Goal(Base) :
    __tablename__ = "goals"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    title: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column()
    date_creation: Mapped[date] = mapped_column(date.today)
    date_conclusion: Mapped[date] = mapped_column()
    