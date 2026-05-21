from fastapi import APIRouter, Depends
from schemas.lead_schema import LeadReceive, LeadResponse, LeadUpdate
from services.lead_service import LeadService
from dependencies import get_lead_service
from models.lead_model import Lead
router = APIRouter(tags=(["Lead"]))

@router.post("/leads", response_model=bool)
def receive_router(schema: LeadReceive, service: LeadService = Depends(get_lead_service)) -> bool :
    return service.save_lead(schema)

@router.get("/leads", response_model=LeadResponse)
def get_lead(id: int, service: LeadService = Depends(get_lead_service)) -> Lead :
    return service.get_lead(id)

@router.put("/leads/{id}", response_model=LeadResponse) 
def update_lead(id: int, schema:LeadUpdate, service: LeadService = Depends(get_lead_service)) :
    return service.update_leads(id, schema)