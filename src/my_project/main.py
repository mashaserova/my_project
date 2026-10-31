import uvicorn

from my_project.setup import app

if __name__ =="__main__":
    uvicorn.run(app)
