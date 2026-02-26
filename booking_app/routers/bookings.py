from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database


router = APIRouter(
    prefix="/bookings",
    tags=["bookings"]
)

@router.post("/", response_model=schemas.BookingRead)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(database.get_db)):
    return crud.create_booking(db, booking)

@router.get("/", response_model=list[schemas.BookingRead])
def list_bookings(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_bookings(db, skip, limit)
