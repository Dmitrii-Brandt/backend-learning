from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, field_validator
from typing import Optional
from enum import Enum



app = FastAPI()

class BookingType(str, Enum):
    kantri = 'kantri'
    full = 'full'
    owner = 'owner'
    

class CottageCreate(BaseModel):
    id: int = Field(gt=0, lt=20)
    house_letter: str = Field(min_length=1, max_length=2)
    beds_num: int = Field(gt=0, lt=20)
    is_booked: bool

    @field_validator("house_letter")
    def must_be_uppercase(cls, value):
        if not value.isupper():
            raise ValueError("house_letter must me uppercase")
        return value

class CottageUpdate(BaseModel):
    house_letter: Optional[str] = None
    beds_num: Optional[int] = None
    is_booked: Optional[bool] = None

class CottageResponse(BaseModel):
    id: int
    house_letter: str
    beds_num: int
    is_booked: bool

cottages = [
    {"id": 1, "house_letter": "A", "beds_num":4, "is_booked": False},
    {"id": 2, "house_letter": "A", "beds_num":4, "is_booked": True},
    {"id": 3, "house_letter": "A", "beds_num":4, "is_booked": False},
    {"id": 4, "house_letter": "A", "beds_num":4, "is_booked": False}
]

@app.get("/cottages/search", response_model=list[CottageResponse])
def search_cottage(beds_num: Optional[int] = Query(None, gt=0)):
    results = cottages
    if beds_num is not None:
        results = [c for c in cottages if c['beds_num'] == beds_num]
    return results

'''new app.get decorator:
1) if function gets number, then searches for cottages with that beds_num
2) if doesn't get number, then returns full cottages list
'''

@app.post("/cottages")
def add_cottage(cottage: CottageCreate):
    cottages.append(cottage.model_dump())
    return {"message": "Cottage added"}

@app.patch("/cottages/{cottage_id}")
def update_cottage(cottage_id: int, updated_data: CottageUpdate):
    for cottage in cottages:
        if cottage['id'] == cottage_id:
            cottage.update(updated_data.model_dump(exclude_unset=True))
            return{"message":"Updated"}
    raise HTTPException(status_code=404, detail="Not found")

'''
1) getting cottage number
2) checking if there cottages with that number
3) changing "is_booked" to oposite value
4) raising error, if not found
'''
@app.patch("/cottages/{cottage_id}/toggle-booking")
def toggle_booking(cottage_id: int):
    for cottage in cottages:
        if cottage['id'] == cottage_id:
            cottage['is_booked'] = not cottage["is_booked"]
            return{"message":f"Cottage nr {cottage_id} is being toggled", "is_booked": cottage["is_booked"]}
    raise HTTPException(status_code=404, detail="Not found")

@app.delete("/cottages/{cottage_id}")
def delete_cottage(cottage_id: int):
    for cottage in cottages:
        if cottage['id'] == cottage_id:
            cottages.remove(cottage)
            return{"message":"Deleted"}
    raise HTTPException(status_code=404, detail="Not found")

print(type(updated_data))