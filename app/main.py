from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import users
from app.db.init_db import create_tables

create_tables()

app = FastAPI(
    title="ITicket API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
