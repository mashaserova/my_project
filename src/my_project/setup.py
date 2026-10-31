from fastapi import FastAPI

from my_project.router import router

app = FastAPI();

app.include_router(router)
