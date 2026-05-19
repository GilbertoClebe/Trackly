from sqlalchemy.orm import Session
from sqlalchemy import select
from models.lead_user import Lead

class LeadService :
    def __init__(self, db: Session) :
        self.db = db
        
    def save_lead(self, lead: Lead) -> bool :
        self.db.add(lead)
        self.db.commit()
        return True

    def get_lead(self, id: int) -> Lead :
        return self.db.get(Lead, id)
    
    def list_leads(self) -> list[Lead] :
        return self.db.scalars(select(Lead))
    
    def update_lead(self, lead: Lead) :
        updated_lead = self.db.merge(lead)
        self.db.commit()
        self.db.refresh(updated_lead)
        return updated_lead
    
    def deactivate_lead(self, lead: Lead) -> Lead :
        deactivated_lead = self.db.merge(lead)
        self.db.commit()
        self.db.refresh(deactivated_lead)
        return deactivated_lead