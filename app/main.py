from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

database = []

class Note(BaseModel):
    title: str
    content: str
    author: str

@app.get('/')
def get_all_data():
    return {'data':database}

@app.get('/{id}')
def get_specific_data(id: int):
    return {'message': f'Requested data for id: {id}'}

@app.post('/')
def create_note(data: Note):
    database.append(data)
    return {'message': data}

@app.put('/{id}')
def update_note(id):
    return {"message":"updating successful"}

