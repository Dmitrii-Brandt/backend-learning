from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class ApartmentBase(BaseModel):
    apt_num: int
    house_letter: str
    bed_amount: int

class ApartmentCreate(ApartmentBase):
    pass

class ApartmentRead(ApartmentBase):
    id:int

    class Config:
        from_attributes = True


class BookingBase(BaseModel):
    client_id: int | None
    apt_id: int
    date_in: date
    date_out: date
    booking_type: str
    persons_num: int

class BookingCreate(BookingBase):
    client_id: int

class BookingRead(BookingBase):
    id: int

    class Config:
        from_attributes = True


class ClientBase(BaseModel):
    name: str
    surname: str | None
    age: int | None = None
    phone_number: str | None = None
    email: str | None = None

class ClientCreate(ClientBase):
    pass

class ClientRead(ClientBase):
    id: int

    class Config:
        from_attributes = True
