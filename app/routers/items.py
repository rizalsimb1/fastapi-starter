from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None

@router.post("/", status_code=201)
async def create_item(item: ItemCreate):
    return {"id": 1, **item.model_dump()}

@router.get("/")
async def list_items(skip: int = 0, limit: int = 20):
    return []
