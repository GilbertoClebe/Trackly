from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

from repository.lead_repository import LeadRepository
from services.lead_service import LeadService

from repository.goal_repository import GoalRepository
from services.goal_service import GoalService
def get_lead_repository(db: Session = Depends(get_db)) :
    return LeadRepository(db)
def get_lead_service(repo: Session = Depends(get_lead_repository)) :
    return LeadService(repo)

def get_goal_repository(db: Session = Depends(get_db)) :
    return GoalRepository(db)
def get_goal_service(repo: GoalService = Depends(get_goal_repository)) :
    return GoalService(repo)