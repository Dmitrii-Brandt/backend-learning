from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey, Identity
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "postgresql://cottages_user:mypassword@localhost:5432/cottages"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base

class Apartment(Base):
    __tablename__ = "apartments"
    id = Column(Integer, Identity(always=True), primary_key=True, index=True)
    apt_num = Column(Integer)
    house_letter = Column(String)
    bed_amount = Column(Integer)
    