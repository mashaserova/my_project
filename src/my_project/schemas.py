from typing import Annotated

from pydantic import BaseModel, EmailStr, StringConstraints


class StatusResponse(BaseModel):
    status: str

class UserCreate(BaseModel):
    login: Annotated[str, StringConstraints(min_length = 1)]
    name: Annotated[str, StringConstraints(min_length = 1)]
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length = 6, max_length = 32)]

class UserResponse(BaseModel):
    name: str
    email: str


class Pet(BaseModel):
    id: int
    name: str
    caption: str

class PetResponse(BaseModel):
    name: str
    caption: str