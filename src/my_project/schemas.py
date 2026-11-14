from typing import Annotated
from pydantic import BaseModel, EmailStr, StringConstraints
from my_project.models import UserRole 


class StatusResponse(BaseModel):
    status: str


class UserCreate(BaseModel):
    login: Annotated[str, StringConstraints(min_length=1)]
    name: Annotated[str, StringConstraints(min_length=1)]
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=6, max_length=32)]


class UserResponse(BaseModel):
    id: int
    login: str
    name: str
    email: str
    role: UserRole


class AnimalCreate(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1)]
    description: Annotated[str, StringConstraints(min_length=1)]
    species: Annotated[str, StringConstraints(min_length=1)]


class AnimalResponse(BaseModel):
    id: int
    name: str
    description: str
    species: str