from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic_core.core_schema import int_schema

from my_project.schemas import StatusResponse, UserCreate, UserResponse
from my_project.schemas import Pet, PetResponse

from my_project.models import User
from my_project.services import UserService

router = APIRouter()

def get_user_service(request: Request)-> UserService:
    return request.app.state.user_service

type UserServiceDep = Annotated[UserService, Depends(get_user_service)]

users_database = dict[str, User]()
petsID_database: dict[int, Pet] = dict[int, Pet]()


@router.get("/status")
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate, user_service: UserServiceDep):
    await user_service.signup(user)


@router.get("/users/{login}")
async def get_user_by_id(id: int, user_service: UserServiceDep) -> UserResponse:
    user = await user_service.get_by_id(id)
    return UserResponse(
        name=user.name,
        email=user.email,
    )


# дз: добавить метод создания id животного и получение этого id (добавить имя, описание и тд)
# + метод возвращающий все данные обо всех животных


@router.post("/create_petID", status_code=status.HTTP_201_CREATED)
def create_petID(pet: Pet) -> None:
    if pet.id in petsID_database:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    petsID_database[pet.id] = pet


@router.get("/{id}/petID")
def get_petID(id: int) -> PetResponse:
    if id not in petsID_database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    pet = petsID_database[id]
    return PetResponse(name=pet.name, caption=pet.caption)


@router.get("/pets")
def get_all_pets() -> list[PetResponse]:
    return [
        PetResponse(name=pet.name, caption=pet.caption)
        for pet in petsID_database.values()
    ]
