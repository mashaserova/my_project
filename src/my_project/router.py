from fastapi import APIRouter, HTTPException, status
from pydantic_core.core_schema import int_schema

from my_project.schemas import StatusResponse, User, UserResponse
from my_project.schemas import Pet, PetResponse

router = APIRouter()

users_database = dict[str, User]()
petsID_database: dict[int, Pet] = dict[int, Pet]()


@router.get("/status")
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: User):
    if user.login in users_database:
        raise HTTPException(status.HTTP_409_CONFLICT)
    users_database[user.login] = user


@router.get("/users/{login}")
def get_user(login: str) -> UserResponse:
    if login not in users_database:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    user = users_database[login]
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
