from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix = "/notes",
    tags=['Notes']
)

@router.get('/')
async def root():
    return {"message": "Root Endpoint"}

@router.get("/{id}")
async def get_note(id: int):
    print(id)
    return {"message": "Get Note Endpoint"}

@router.post("/")
async def create_note():
    return {"message": "Create Note Endpoint"}

@router.put("/{id}")
async def update_note(id: int):
    print(id)
    return {"message": "Update Note Endpoint"}

@router.delete("/{id}")
async def delete_note(id: int):
    print(id)
    return {"message": "Delete Note Endpoint"}