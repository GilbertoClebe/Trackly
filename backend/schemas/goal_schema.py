from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import Enum

class STATUS(Enum) :
    NOT_STARTED = "not_started"
    IN_PROCESS = "in_process"
    FINISHED = "finished"

class Goalbase(BaseModel) :
    status: STATUS
    title: str
    description: str
    
class GoalCreate(Goalbase) :
    model_config = ConfigDict(from_attributes=True)
    
class GoalUpdate(Goalbase) :
    status: Optional[STATUS] = None
    title: Optional[str] = None
    description: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

    