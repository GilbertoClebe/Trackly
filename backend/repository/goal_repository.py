from sqlalchemy.orm import Session
from sqlalchemy import delete, select, update
from models.goal_model import Goal


class GoalRepository :
    def __init__(self, db: Session) :
        self.db = db
    
    def create_goal(self, goal: Goal) -> Goal :
        self.db.add(goal)
        self.db.commit()
        self.db.refresh(goal)
        return goal
    
    def get_goal(self, id: int) -> Goal :
        return self.db.get(Goal, id)
    
    def list_goal(self) -> list[Goal] :
        return list[self.db.scalars(select(Goal)).all()]
    
    def update_goal(self, id: int, new_goal: Goal) -> Goal :
        goal = self.db.get(Goal, id)
        
        goal.title = new_goal.title
        goal.description = new_goal.description
        goal.status = new_goal.status
        
        self.db.commit()
        return goal
    
    def delete_goal(self, id: int) -> None :
        self.db.execute(delete(Goal).where(Goal.id == id))
        self.db.commit()
        return None