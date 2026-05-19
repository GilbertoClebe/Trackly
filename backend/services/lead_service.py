from repository.lead_repository import LeadRepository
from models.lead_model import Lead
from schemas.lead_schema import LeadReceive, LeadUpdate
class LeadService :
    def __init__(self, repo: LeadRepository) :
        self.repo = repo
        
    def save_lead(self, schema: LeadReceive) -> bool :
        return self.repo.save_lead(self.receive_to_lead(schema))
    
    def get_lead(self, id: int) -> Lead :
        return self.repo.get_lead(id)
    
    def list_leads(self) -> list[Lead] :
        return self.repo.list_leads()
    
    def update_leads(self, schema: LeadUpdate) -> Lead :
        return self.repo.update_lead(self.update_to_lead(schema))
    
    def receive_to_lead(self, schema: LeadReceive) : 
        return Lead(
            name = schema.name,
            last_name = schema.last_name,
            number = schema.number,
            email = schema.email,
            address = schema.address,
            birthdate = schema.birthdate,
            occupation = schema.occupation,
            status = schema.status
        )
        
    def update_to_lead(self, schema: LeadUpdate) -> Lead :
        return Lead(
            status = schema.status
        )

    def deactivate_lead(self, id: int) -> Lead :
        lead = self.get_lead(id)
        return self.deactivate_lead(lead)