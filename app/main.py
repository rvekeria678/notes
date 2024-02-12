from fastapi import FastAPI
from .routers import note, user, auth

app = FastAPI()


app.include_router(note.router)