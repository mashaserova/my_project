from fastapi import HTTPException, status

from my_project.models import User, UserRole, Animal
from my_project.repositories import UserRepository, AnimalRepository
from my_project.schemas import UserCreate, AnimalCreate


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    async def signup(self, user_data: UserCreate) -> User:
        if await self.__user_repository.get_by_login(user_data.login):
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Login already exists")
        
        if await self.__user_repository.get_by_email(user_data.email):
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Email already exists")

        all_users = await self.__user_repository.get_all()
        role = UserRole.ADMIN if len(all_users) == 0 else UserRole.USER
        
        model = User(
            id=0,
            login=user_data.login,
            name=user_data.name,
            role=role,
            email=user_data.email,
            password=user_data.password,
        )

        await self.__user_repository.save(model)
        return model

    async def get_by_id(self, id: int) -> User:
        model = await self.__user_repository.get_by_id(id)
        if model is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
        return model
    
    async def get_all(self) -> list[User]:
        return await self.__user_repository.get_all()


class AnimalService:
    def __init__(self, animal_repository: AnimalRepository):
        self.__animal_repository = animal_repository

    async def create_animal(self, animal_data: AnimalCreate) -> Animal:
        animal = Animal(
            id=0,
            name=animal_data.name,
            description=animal_data.description,
            species=animal_data.species
        )
        await self.__animal_repository.save(animal)
        return animal

    async def get_animal_by_id(self, id: int) -> Animal:
        animal = await self.__animal_repository.get_by_id(id)
        if animal is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Animal not found")
        return animal

    async def get_all_animals(self) -> list[Animal]:
        return await self.__animal_repository.get_all()