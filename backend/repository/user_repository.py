from models.user_model import User
from sqlalchemy import select
from sqlalchemy.orm import Session

class UserRepository :
    def __init__(self, db: Session) :
        self.db = db
    
    def create_user(self, user: User) -> bool :
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return True
    
    def get_user(self, id) -> User :
        return self.db.get(User, id)
    
    def list_user(self) -> list[User] :
        return self.db.scalars(select(User)).all()
    
    def update_user(self, user: User) -> User :
        self.db.merge(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    
    def deactivate_user(self, id: int) -> bool :
        user = self.db.get(User, id)
        user.active = False
        self.db.commit()
        self.db.refresh(user)
        return True
    