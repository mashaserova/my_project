from pydantic import BaseModel


class StatusResponse(BaseModel):
    status: str


class UserResponse(BaseModel):
    name: str
    email: str


class User(BaseModel):
    login: str
    name: str
    email: str
    password: str

class Pet(BaseModel):
    id: int
    name: str
    caption: str

class PetResponse(BaseModel):
    name: str
    caption: str