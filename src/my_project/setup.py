from fastapi import FastAPI

from my_project.repositories import UserRepository, AnimalRepository
from my_project.router import router
from my_project.services import UserService, AnimalService

app = FastAPI()

user_repository = UserRepository()
app.state.user_service = UserService(user_repository)

animal_repository = AnimalRepository()
app.state.animal_service = AnimalService(animal_repository)

app.include_router(router)