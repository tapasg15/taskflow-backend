from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
    name:str
    email:str
    password:str
    
class UserOut(BaseModel):
    id:int
    name:str
    email:str
    created_at:datetime
    
    class config:
        from_attributes = True
        
        
class ProjectCreate(BaseModel):
    name:str
    description:str | None = None
    owner_id:int  
    
class ProjectOut(BaseModel):
    id:int
    name:str
    description:str | None = None
    owner_id: int | None = None
    created_at: datetime
        
              
class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    project_id: int
    
class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    status: str |None = None
    
class TaskOut(BaseModel):
    id: int
    title: str
    description: str |None = None
    status: str
    project_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True