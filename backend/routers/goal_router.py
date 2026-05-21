from fastapi import APIRouter, Depends
from dependencies import get_goal_service
from services.goal_service import GoalService
from models.goal_model import Goal
from schemas.goal_schema import GoalCreate, GoalUpdate, GoalResponse

router = APIRouter(tags=(["Goal"]))

@router.post("/goals", response_model=GoalResponse)
def create_goal(schema: GoalCreate, service: GoalService = Depends(get_goal_service)) -> Goal :
    return service.create_goal(schema)

@router.get("/goals/{id}", response_model=GoalResponse) 
def get_goal(id: int, service: GoalService = Depends(get_goal_service)) -> Goal :
        return service.get_goal(id)
    
@router.put("/goals/{id}", response_model=GoalResponse)
def update_goal(id: int, schema: GoalUpdate, service: GoalService = Depends(get_goal_service)) -> Goal :
    return service.update_goal(id, schema)
    
@router.delete("/router/{id}", response_model=None)
def delete_goal(id: int, service: GoalService = Depends(get_goal_service)) -> None :
    return service.delete_goal(id)