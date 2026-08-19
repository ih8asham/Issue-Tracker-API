from pydantic import BaseModel, ConfigDict

class IssueCreate(BaseModel):
    title: str
    description: str
    category: str
    priority: str  
    
class IssueUpdate(BaseModel):
    title: str | None = None
    description: str |None = None
    category: str | None = None
    priority: str | None = None 
    status: str | None = None 
    
class IssueOut(BaseModel):
    id: int 
    title: str
    description: str
    category: str
    priority: str
    status: str 

    model_config = ConfigDict(from_attributes= True) 