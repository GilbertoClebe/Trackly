from sqlalchemy.orm import Session
from sqlalchemy import select
from models.chat_model import Chat

class ChatRepository :
    def __init__(self, db: Session) :
        self.db = db
        
    def save_history(self, chat: Chat) -> bool :
        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)
        return True
    
    def list_history(self) -> list[Chat] :
        return self.db.scalars(select(Chat)).all()