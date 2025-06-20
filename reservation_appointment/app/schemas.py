from pydantic import BaseModel,EmailStr
from datetime import datetime


class AppointmentBase(BaseModel):
    client_name: str
    client_email: EmailStr
    appointment_date: datetime


class AppointmentCreate(AppointmentBase):
    ...   

class AppointmentRead(AppointmentBase):
    
    id: int

    class Config:
        from_attributes = True   
