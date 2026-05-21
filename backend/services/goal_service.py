from repository.goal_repository import GoalRepository
from schemas.goal_schema import GoalCreate, GoalUpdate
from models.goal_model import Goal
class GoalService :
    def __init__(self, repo: GoalRepository) :
        self.repo = repo
        
    def create_goal(self, schema: GoalCreate) -> Goal :
        goal = self.parse_create_to_goal(schema)
        return self.repo.create_goal(goal)
    
    def get_goal(self, id: int) -> Goal :
        return self.repo.get_goal(id)
    
    def list_goals(self) -> list[Goal] :
        return self.repo.list_goal()
    
    def update_goal(self, id: int, schema: GoalUpdate) -> Goal :
        goal = self.update_to_goal(schema)
        return self.repo.update_goal(id, goal)
    
    def delete_goal(self, id: int) -> None :
        return self.repo.delete_goal(id)
        
    def parse_create_to_goal(self, schema: GoalCreate) -> Goal :
        return Goal(
            status = schema.status.value,
            title = schema.title,
            description = schema.description
        )
        
    def update_to_goal(self, schema: GoalUpdate) -> Goal :
        return Goal(
            status = schema.status.value,
            title = schema.title,
            description = schema.description
        )