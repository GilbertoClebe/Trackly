from pydantic import BaseModel, ConfigDict, Field

#terminar depois que tiver os dados tratados.
class DashLeadResponse(BaseModel) :
    model_config = ConfigDict(from_attributes=True)
    
class DashGoalResponse(BaseModel) :
    model_config = ConfigDict(from_attributes=True)
    
class DashUserResponse(BaseModel) :
    model_config = ConfigDict(from_attributes=True)