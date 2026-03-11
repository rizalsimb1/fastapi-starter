from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, EmailStr
from ..database import get_db

router = APIRouter()

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    is_active: bool
    class Config:
        from_attributes = True

@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    raise NotImplementedError("Implement user creation")

@router.get("/me", response_model=UserResponse)
async def get_me():
    raise NotImplementedError("Implement current user retrieval")
