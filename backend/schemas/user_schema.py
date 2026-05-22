from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Optional
from datetime import date
from enum import Enum

class Role(Enum):
    """Enumeration defining the systemic access levels and organizational roles for a user."""
    ADMINISTRATOR = "ADM"
    EMPLOYEE = "EMP"

class UserBase(BaseModel):
    """Base structural data model defining the core shared profile attributes for a system user."""
    name: str = Field(description="The full legal name of the user record owner.")
    email: str = Field(description="The primary email address string used for user correspondence and system identification.")
    number: str = Field(max_length=11, description="The contact phone number, containing only numeric digits including the area code. Maximum allowed length is 11 characters.")
    CPF: str = Field(min_length=11, max_length=11, description="The official 11-digit Brazilian physical person register identity number (Cadastro de Pessoas Físicas), containing only numbers.")
    address: str = Field(description="The complete residential or mailing street address provided by the user.")
    role: Role = Field(description="The systemic authorization role level designated for the user ('ADM' or 'EMP').")
    
class UserCreate(UserBase):
    """Data validation schema utilized strictly for parsing and sanitizing account configurations during new user provisioning."""
    password: str = Field(description="The plain-text raw password chosen by the user, to be securely hashed and encrypted upon ingestion.")
    model_config = ConfigDict(from_attributes=True)
    
class UserResponse(UserBase):
    """Data serialization schema representing the complete public profile dataset of a user retrieved from storage."""
    active: bool = Field(description="A boolean flag signaling whether the user account is operationally active and permitted to authenticate.")
    model_config = ConfigDict(from_attributes=True)
    
class UserUpdate(BaseModel):
    """Delta mutation schema optimized for executing partial profile modifications (PATCH operations) on an existing user instance. All fields are optional; omit any attributes that should remain unchanged."""
    name: Optional[str] = Field(default=None, description="The updated full name of the user. Omit or pass null if keeping the current value.")
    email: Optional[str] = Field(default=None, description="The updated primary email address string. Omit or pass null if keeping the current value.")
    number: Optional[str] = Field(default=None, max_length=11, min_length=11, description="The updated 11-digit contact phone number. Must be exactly 11 characters if provided.")
    CPF: Optional[str] = Field(default=None, max_length=11, min_length=11, description="The updated 11-digit Brazilian CPF registration string. Must be exactly 11 characters if provided.")
    address: Optional[str] = Field(default=None, description="The updated residential or mailing address string. Omit or pass null if keeping the current value.")
    role: Optional[Role] = Field(default=None, description="The updated authorization role tier for the user account. Omit if keeping current tier.")
    password: Optional[str] = Field(default=None, description="A new raw credentials string to replace the existing user password. Omit if the password remains unchanged.")
    active: Optional[bool] = Field(default=None, description="An updated boolean flag toggle to alter the active state and access status of the user account.")
    model_config = ConfigDict(from_attributes=True)