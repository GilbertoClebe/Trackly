from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

from repository.lead_repository import LeadRepository
from services.lead_service import LeadService

def get_lead_repository(db: Session = Depends(get_db)) :
    return LeadRepository(db)
def get_lead_service(repo: Session = Depends(get_lead_repository)) :
    return LeadService(repo)