from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

'''
database.py

create_engine
SessionLocal
Base
get_db dependency
Only DB setup lives here.'''


DATABASE_URL = "postgresql://cottages_user:mypassword@localhost:5432/cottages"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
