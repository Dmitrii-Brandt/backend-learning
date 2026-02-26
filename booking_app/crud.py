from sqlalchemy.orm import Session
from . import models, schemas


def create_apartment(db: Session, apartment: schemas.ApartmentCreate):
    db_apartment = models.Apartment(**apartment.model_dump())
    db.add(db_apartment)
    db.commit()
    db.refresh(db_apartment)
    return db_apartment

def get_apartments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Apartment).offset(skip).limit(limit).all()

def create_booking(db: Session, booking: schemas.BookingCreate):
    db_booking = models.Bookings(**booking.model_dump())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def get_bookings(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Bookings).offset(skip).limit(limit).all()

def create_client(db: Session, client: schemas. ClientCreate):
    db_client = models.Clients(**client.model_dump())
    db.add(db_client)
    db.commit
    db.refresh(db_client)
    return db_client

def get_clients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Clients).offset(skip).limit(limit).all()
