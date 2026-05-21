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
    
    def update_leads(self, id: int, schema: LeadUpdate) -> Lead :
        status_novo = self.update_to_lead(schema)
        return self.repo.update_lead(id, status_novo)
    
    def receive_to_lead(self, schema: LeadReceive) : 
        return Lead(
            name = schema.name,
            last_name = schema.last_name,
            number = schema.number,
            email = schema.email,
            address = schema.address,
            birthdate = schema.birthdate,
            occupation = schema.occupation,
            date_update = None,
            status = schema.status.value
        )
        
    def update_to_lead(self, schema: LeadUpdate) -> Lead :
        return Lead(
            status = schema.status.value
        )
