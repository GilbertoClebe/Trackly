from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class STATUS(Enum):
    """Enumeration representing the execution states of a goal or task lifecycle."""
    NOT_STARTED = "not_started"
    IN_PROCESS = "in_process"
    FINISHED = "finished"

class Goalbase(BaseModel):
    """Base structural data model defining the core shared attributes for a goal entity."""
    status: STATUS = Field(description="The current operational state of the goal. Must map to a defined lifecycle phase (e.g., 'not_started', 'in_process', 'finished').")
    title: str = Field(description="A concise, high-level name or headline specifying the objective of the goal.")
    description: str = Field(description="A detailed contextual description explaining the exact requirements and parameters needed to fulfill the goal.")
    
class GoalCreate(Goalbase):
    """Data validation schema utilized strictly for parsing and sanitizing payloads during new goal creation."""
    model_config = ConfigDict(from_attributes=True)
    
class GoalUpdate(Goalbase):
    """Delta mutation schema optimized for executing partial updates (PATCH operations) on existing goal instances. All fields are optional; omit any attributes that should remain unchanged."""
    status: Optional[STATUS] = Field(default=None, description="The new operational state to apply. Omit or pass null if keeping the current status.")
    title: Optional[str] = Field(default=None, description="The updated headline for the goal. Omit or pass null if keeping the current title.")
    description: Optional[str] = Field(default=None, description="The updated detailed description text. Omit or pass null if keeping the current description.")
    model_config = ConfigDict(from_attributes=True)

class GoalResponse(Goalbase):
    """Data serialization schema representing the complete goal record structure as retrieved from persistent storage."""
    id: int = Field(description="The unique database primary key integer identifying this specific goal instance.")
    date_creation: date = Field(description="The system-generated calendar date when this goal record was initially instantiated. Format: YYYY-MM-DD.")
    date_conclusion: date = Field(default=None, description="The calendar date when the goal's status was officially changed to 'finished'. Format: YYYY-MM-DD. Evaluates to null if the goal is ongoing.")
    model_config = ConfigDict(from_attributes=True)