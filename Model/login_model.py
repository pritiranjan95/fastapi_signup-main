from pydantic import BaseModel, Field, EmailStr
import uuid

class Login(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    mail_id: EmailStr
    password:str
