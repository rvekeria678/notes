from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class Base_Note(BaseModel):
    title : str
    content : str

class Note(Base_Note):
    id: int
    created_at : datetime
    owner_id: int
    

class Return_Note(BaseModel)