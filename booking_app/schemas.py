from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class ApartmentCreate(BaseModel):
    apt_num: int
    house_letter: str
    bed_amount: int

class ApartmentRead(ApartmentCreate):
    id:int

    class Config:
        orm_mode = True

class BookingCreate(BaseModel):
    client_id: int
    apt_id: int
    date_in: date
    date_out: date
    booking_type: str
    persons_num: int
    created_at: datetime

class BookingRead(BookingCreate):
    id: int

    class Config:
        orm_mode = True

"add clients class here!!! "