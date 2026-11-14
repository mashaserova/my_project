from typing import Annotated

from fastapi import APIRouter, Depends, Request, status

from my_project.models import User, Animal
from my_project.schemas import (
    StatusResponse, UserCreate, UserResponse, AnimalCreate, AnimalResponse
)
from my_project.services import UserService, AnimalService

router = APIRouter()


def get_user_service(request: Request) -> UserService:
    return request.app.state.user_service


def get_animal_service(request: Request) -> AnimalService:
    return request.app.state.animal_service


type UserServiceDep = Annotated[UserService, Depends(get_user_service)]
type AnimalServiceDep = Annotated[AnimalService, Depends(get_animal_service)]


@router.get("/status")
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")


# --- USER ROUTES ---

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserCreate, user_service: UserServiceDep) -> dict[str, int | str]:
    user = await user_service.signup(user_data)
    return {"id": user.id, "message": "User created"}


@router.get("/users")
async def get_all_users(user_service: UserServiceDep) -> list[UserResponse]:
    users = await user_service.get_all()
    return [
        UserResponse(
            id=u.id,
            login=u.login,
            name=u.name,
            email=u.email,
            role=u.role
        )
        for u in users
    ]


@router.get("/users/{id}")
async def get_user_by_id(id: int, user_service: UserServiceDep) -> UserResponse:
    user = await user_service.get_by_id(id)
    return UserResponse(
        id=user.id,
        login=user.login,
        name=user.name,
        email=user.email,
        role=user.role
    )


@router.post("/animals", status_code=status.HTTP_201_CREATED)
async def create_animal(
    animal_data: AnimalCreate,
    animal_service: AnimalServiceDep
) -> dict[str, int | str]:
    animal = await animal_service.create_animal(animal_data)
    return {"id": animal.id, "message": "Animal created"}


@router.get("/animals/{id}")
async def get_animal_by_id(
    id: int,
    animal_service: AnimalServiceDep
) -> AnimalResponse:
    animal = await animal_service.get_animal_by_id(id)
    return AnimalResponse(
        id=animal.id,
        name=animal.name,
        description=animal.description,
        species=animal.species
    )


@router.get("/animals")
async def get_all_animals(
    animal_service: AnimalServiceDep
) -> list[AnimalResponse]:
    animals = await animal_service.get_all_animals()
    return [
        AnimalResponse(
            id=a.id,
            name=a.name,
            description=a.description,
            species=a.species
        )
        for a in animals
    ]