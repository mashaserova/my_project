from fastapi import HTTPException, status

from my_project.models import User, UserRole
from my_project.repositories import UserRepository
from my_project.schemas import UserCreate

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    async def signup(self, user: UserCreate)-> User:
        all_users = await self.__user_repository.get_all()
        if len(all_users) == 0:
            role = UserRole.ADMIN # в начале база пустая, первый пользователь - админ
        else:
            role = UserRole.USER
        
        model = User(
            id=0,
            login=user.login,
            name=user.name,
            role=role,
            email=user.email,
            password=user.password,
        )

        await self.__user_repository.save(model)
        return model



    async def get_by_id(self, id: int)-> User:
        model = await self.__user_repository.get_by_id(id)
        if model is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail = "User was not found")
        return model
    
    async def get_all(self) -> list[User]:
        return await self.__user_repository.get_all()