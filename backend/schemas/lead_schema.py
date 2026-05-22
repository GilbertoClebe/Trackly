from pydantic import BaseModel, ConfigDict, Field, EmailStr
from enum import Enum
from datetime import date
from typing import Optional

class STATUS(Enum):
    """Enumeration representing the qualification lifecycle stages of a sales lead."""
    UNQUALIFIED = "unqualified"
    QUALIFIED = "qualified"
    CONVERTED = "converted"

class LeadUpdate(BaseModel):
    """Data validation schema optimized for updating the lifecycle stage of an existing lead."""
    status: STATUS = Field(description="The updated qualification lifecycle state to apply to the lead record.")
    model_config = ConfigDict(from_attributes=True)
    
class LeadResponse(BaseModel):
    """Data serialization schema representing a complete lead record retrieved from persistent storage."""
    name: str = Field(max_length=120, description="The given or first name of the lead. Maximum allowed length is 120 characters.")
    last_name: str = Field(max_length=120, description="The family name or surname of the lead. Maximum allowed length is 120 characters.")
    number: str = Field(max_length=11, min_length=11, description="The 11-digit contact phone number, containing only numeric digits including the area code. Must be exactly 11 characters.")
    email: EmailStr = Field(description="The validated primary email address belonging to the lead.")
    address: str = Field(description="The physical residential or mailing address provided by the lead.")
    birthdate: date = Field(description="The calendar date of birth for the lead. Format: YYYY-MM-DD.")
    occupation: str = Field(description="The current professional role, job title, or field of employment of the lead.")
    status: STATUS = Field(description="The current qualification lifecycle state assigned to the lead record.")
    date_access: date = Field(description="The calendar date when this lead record was most recently accessed or reviewed. Format: YYYY-MM-DD.")
    date_update: Optional[date] = Field(default=None, description="The calendar date when the lead record details were last modified. Format: YYYY-MM-DD. Evaluates to null if never updated.")
    model_config = ConfigDict(from_attributes=True)

class LeadReceive(BaseModel):
    """Inbound data schema for receiving, parsing, and validating new lead record submissions."""
    name: str = Field(max_length=120, description="The given or first name of the incoming lead. Maximum allowed length is 120 characters.")
    last_name: str = Field(max_length=120, description="The family name or surname of the incoming lead. Maximum allowed length is 120 characters.")
    number: str = Field(max_length=11, min_length=11, description="The 11-digit contact phone number provided by the inbound source, containing only numbers. Must be exactly 11 characters.")
    email: EmailStr = Field(description="The raw email address string submitted by the incoming lead pipeline.")
    address: str = Field(description="The physical address string supplied within the lead payload.")
    birthdate: date = Field(description="The calendar date of birth submitted for the incoming lead. Format: YYYY-MM-DD.")
    occupation: str = Field(description="The stated professional role or occupation of the incoming lead.")
    status: STATUS = Field(description="The initial operational qualification status designated for this inbound lead payload.")
    date_update: Optional[date] = Field(default=None, description="An optional historical modification timestamp provided by the external source. Format: YYYY-MM-DD.")
    model_config = ConfigDict(from_attributes=True)