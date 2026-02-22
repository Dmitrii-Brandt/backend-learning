from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, field_validator
from typing import Optional

app = FastAPI()

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

@app.get("/cottages", response_model=list[CottageResponse])
def get_cottages():
    return cottages

@app.post("/cottages")
def add_cottage(cottage: CottageCreate):
    cottages.append(cottage.model_dump())
    return {"message": "Cottage added"}

@app.put("/cottages/{cottage_id}")
def update_cottage(cottage_id: int, updated_data: CottageUpdate):
    for cottage in cottages:
        if cottage['id'] == cottage_id:
            cottage.update(updated_data)
            return{"message":"Updated"}
    raise HTTPException(status_code=404, detail="Not found")

@app.delete("/cottages/{cottage_id}")
def delete_cottage(cottage_id: int):
    for cottage in cottages:
        if cottage['id'] == cottage_id:
            cottages.remove(cottage)
            return{"message":"Deleted"}
    raise HTTPException(status_code=404, detail="Not found")