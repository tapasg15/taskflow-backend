from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("", response_model = schemas.ProjectOut)
def create_project(data: schemas.ProjectCreate, db:Session = Depends(get_db)):
    owner = db.query(models.User).filter(models.User.id == data.owner_id).first()
    if not owner:
        raise HTTPException(status_code=404, detail="Owner (user) not found")
    
    project = models.Project(**data.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

@router.get("", response_model=list[schemas.ProjectOut])
def list_projects(db:Session = Depends(get_db)):
    return db.query(models.Project).all()

@router.get("/{project_id}/tasks", response_model=list[schemas.TaskOut])
def get_project_tasks(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project.tasks

