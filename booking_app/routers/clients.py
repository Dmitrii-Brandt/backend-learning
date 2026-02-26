from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database


router = APIRouter(
    prefix="/clients",
    tags=["clients"]
)

@router.post("/", response_model=schemas.ClientRead)
def create_client(booking: schemas.ClientCreate, db: Session = Depends(database.get_db)):
    return crud.create_booking(db, booking)

@router.get("/", response_model=list[schemas.ClientRead])
def list_clients(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_clients(db, skip, limit)