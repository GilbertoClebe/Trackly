from sqlalchemy.orm import Session
from sqlalchemy import update
from models.lead_model import Lead

class LeadRepository :
    def __init__(self, db: Session) :
        self.db = db
        
    def save_lead(self, lead: Lead) -> bool :
        self.db.add(lead)
        self.db.commit()
        return True

    def get_lead(self, id: int) -> Lead :
        return self.db.get(Lead, id)
    
    def update_lead(self, id: int, status_novo: str) -> Lead:
        lead = self.db.get(Lead, id)
        lead.status = status_novo
        self.db.execute(update(Lead).where(Lead.id == id).values(status = status_novo))
        
        self.db.commit()
        self.db.refresh(lead)
        return lead