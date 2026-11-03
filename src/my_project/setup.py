from fastapi import FastAPI

from my_project.repositories import UserRepository
from my_project.router import router
from my_project.services import UserService

app = FastAPI();
user_repository = UserRepository()
app.state.user_service = UserService(user_repository)

app.include_router(router)
