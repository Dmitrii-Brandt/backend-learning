from sqlalchemy import Column, Integer, Identity, String, ForeignKey, Date, text
from sqlalchemy import DateTime, CheckConstraint, Enum
from .database import Base
'''Only SQLAlchemy ORM models:
Apartment
Client
Booking
No FastAPI code here.'''

BookingTypeEnum = Enum(
    "kantri",
    "full",
    "owner",
    name="booking_type_enum"
)

class Apartment(Base):
    __tablename__ = "apartments"

    id = Column(Integer, Identity(always=True), primary_key=True, index=True)
    apt_num = Column(Integer, nullable=False)
    house_letter = Column(String)
    bed_amount = Column(Integer, nullable=False)
    
class Clients(Base):
    __tablename__ = "clients"

    id = Column(Integer, Identity(always=True), primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String)
    age = Column(Integer)
    phone_number = Column(String)
    email = Column(String)

class Bookings(Base):
    __tablename__ = "bookings"

    id = Column(Integer, Identity(always=True), primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="SET NULL"), nullable=True)
    date_in = Column(Date, nullable=False)
    date_out = Column(Date, nullable=False)
    persons_num = Column(Integer, server_default=text("1"), nullable=False)
    apt_id = Column(Integer, ForeignKey("apartments.id"), nullable=False)
    created_at = Column(DateTime, server_default=text("now()"))
    booking_type = Column(BookingTypeEnum, nullable=False)

    __table_args__ = (
        CheckConstraint("date_in < date_out", name="date_validity"),
    )