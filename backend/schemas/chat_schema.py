from pydantic import BaseModel, ConfigDict, Field

class Prompt(BaseModel) :
    prompt: str = Field(max_length=500)
    model_config = ConfigDict(from_attributes=True)
    
class Response(BaseModel) :
    message: str
    model_config = ConfigDict(from_attributes=True)

    