from pydantic import BaseModel, Field, EmailStr
import uuid


class UserdataModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    first_name:str
    last_name: str
    mail_id: EmailStr
    password: str

class UserToSee(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    first_name:str
    last_name: str
    mail_id: EmailStr

    