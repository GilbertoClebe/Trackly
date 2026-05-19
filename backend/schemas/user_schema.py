from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Optional
from datetime import date
from enum import Enum

class Role(Enum) :
    ADMINISTRATOR = "ADM"
    EMPLOYEE = "EMP"

class UserBase(BaseModel) :
    name: str
    email: str
    number: str = Field(max_length=11, min_length=11)
    CPF: str = Field(max_length=11, min_length=11)
    address: str
    role: Role
    
class UserCreate(UserBase) :
    model_config = ConfigDict(from_attributes=True)
    
class UserResponse(UserBase) :
    active: bool
    model_config = ConfigDict(from_attributes=True)
    
class UserUpdate(BaseModel) :
    name: Optional[str] = None
    email: Optional[str] = None
    number: Optional[str] = Field(max_length=11, min_length=11) | None
    CPF: Optional[str] = Field(max_length=11, min_length=11) | None
    address: Optional[str] = None
    role: Optional[Role] = None
    date_creation: Optional[date] = None
    active: Optional[bool] = None
    model_config = ConfigDict(from_attributes=True)