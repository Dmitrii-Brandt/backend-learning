from fastapi import FastAPI
from .database import Base, engine
from .routers import apartments, clients, bookings

#create tables (only in dev)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(apartments.router)
app.include_router(clients.router)
app.include_router(bookings.router)