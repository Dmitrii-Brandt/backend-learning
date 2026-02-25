from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database


router = APIRouter(
    prefix="/apartments",
    tags=["apartments"]
)

@router.post("/", response_model=schemas.ApartmentRead)
def create_apartment(apartment: schemas.ApartmentCreate, db: Session = Depends(database.get_db)):
    return crud.create_apartment(db, apartment)

@router.get("/", response_model=list[schemas.ApartmentRead])
def list_apartments(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_apartments(db, skip, limit)
