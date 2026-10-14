from fastapi import FastAPI

from .import models
from .database import engine
from .routers import users, projects, tasks

models.Base.metadata.create_all(bind = engine) 

app = FastAPI(title = "TaskFlow")

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)
