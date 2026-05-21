from pydantic import BaseModel, ConfigDict, Field, EmailStr
from enum import Enum
from datetime import date
from typing import Optional

class STATUS(Enum) :
    UNQUALIFIED = "unqualified"
    QUALIFIED = "qualified"
    CONVERTED = "converted"

class LeadUpdate(BaseModel) :
    status: STATUS
    model_config = ConfigDict(from_attributes=True)
    
class LeadResponse(BaseModel) :
    name: str = Field(max_length=120)
    last_name: str = Field(max_length=120)
    number: str = Field(max_length=11, min_length=11)
    email: EmailStr
    address: str
    birthdate: date
    occupation: str
    status: STATUS
    date_access: date
    date_update: Optional[date] = None
    model_config = ConfigDict(from_attributes=True)

class LeadReceive(BaseModel) :
    name: str = Field(max_length=120)
    last_name: str = Field(max_length=120)
    number: str = Field(max_length=11, min_length=11)
    email: str
    address: str
    birthdate: date
    occupation: str
    status: STATUS
    date_update: Optional[date] = None
    model_config = ConfigDict(from_attributes=True)
