from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
from database import Base
from datetime import date

class Chat(Base) :
    __tablename__ = "chat"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    prompt: Mapped[str] = mapped_column(String(500))
    message: Mapped[str] = mapped_column(Text)
    date_requisition: Mapped[date] = mapped_column(date.today)
    