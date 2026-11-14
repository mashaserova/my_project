from enum import StrEnum
from pydantic import BaseModel


class UserRole(StrEnum):
    USER = "USER"
    ADMIN = "ADMIN"


class User(BaseModel):
    id: int
    login: str
    name: str
    role: UserRole
    email: str
    password: str


class Animal(BaseModel):
    id: int
    name: str
    description: str
    species: str