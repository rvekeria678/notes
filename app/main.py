from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Root Endpoint"}

@app.get("/{id}")
async def get_note(id: int):
    print(id)
    return {"message": "Get Note Endpoint"}

@app.post("/")
async def create_note():
    return {"message": "Create Note Endpoint"}

@app.put("/{id}")
async def update_note(id: int):
    print(id)
    return {"message": "Update Note Endpoint"}

@app.delete("/{id}")
async def delete_note(id: int):
    print(id)
    return {"message": "Delete Note Endpoint"}