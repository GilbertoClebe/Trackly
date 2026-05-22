# Lead File
from fastapi import APIRouter, Depends, status
from schemas.lead_schema import LeadReceive, LeadResponse, LeadUpdate
from services.lead_service import LeadService
from dependencies import get_lead_service
from models.lead_model import Lead

router = APIRouter(tags=(["Lead"]))

@router.post("/leads", response_model=LeadResponse, status_code=status.HTTP_201_CREATED)
def receive_router(schema: LeadReceive, service: LeadService = Depends(get_lead_service)) -> LeadResponse :
    """Ingest and persist a new sales lead or prospect record.

    **AI Agent Context:**
    Trigger this endpoint when a new prospect is acquired via inbound marketing forms, 
    external lead generation providers, or manual CRM entry. The response yields the 
    fully persisting lead entity including its newly generated system `id` for subsequent 
    tracking workflow automation.

    * **Pre-conditions:** The payload must contain valid contact information (email or phone). 
        Duplicate detection algorithms will reject the payload if a matching record exists.
    * **Permissions:** Requires `lead:write` scopes.

    **Side-Effects:**
    * Dispatches an asynchronous webhook to the central CRM system.
    * Triggers a targeted automated welcome email via the marketing service.
    * Enqueues a background task for data enrichment (e.g., Clearbit/ZoomInfo lookup).
    """
    return service.save_lead(schema)

@router.get("/leads/{id}", response_model=LeadResponse)
def get_lead(id: int, service: LeadService = Depends(get_lead_service)) -> Lead :
    """Retrieve the comprehensive profile and metadata of a specific lead.

    **AI Agent Context:**
    Trigger this endpoint to fetch detailed context about a prospect before initiating 
    outreach, or to display lead details within the sales qualification dashboard.

    * **Pre-conditions:** The specific lead ID must exist in the database.
    * **Permissions:** Requires `lead:read` scopes.

    **Side-Effects:**
    * Emits a read-receipt audit log event to track data access compliance.
    """
    return service.get_lead(id)

@router.put("/leads/{id}", response_model=LeadResponse) 
def update_lead(id: int, schema: LeadUpdate, service: LeadService = Depends(get_lead_service)) :
    """Modify the canonical record of an existing lead via full replacement.

    **AI Agent Context:**
    Trigger this endpoint when a prospect's demographic data, qualification status, 
    or contact information changes during the sales pipeline progression and a full 
    resource override is intended.

    * **Pre-conditions:** The lead must currently exist and not be in a "converted" state.
    * **Permissions:** Requires `lead:write` scopes.

    **Side-Effects:**
    * Asynchronously propagates state changes to downstream data warehouses (e.g., Snowflake).
    * Invalidates distributed cache entries associated with this lead ID.
    """
    return service.update_leads(id, schema)