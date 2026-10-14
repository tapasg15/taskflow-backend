from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix = "/tasks", tags = ["Tasks"])

@router.post("", response_model = schemas.TaskOut)
def create_task(data: schemas.TaskCreate, db:Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == data.project_id).first()
    if not project:
        raise HTTPException(ststus_code = 404, detail = "Project not found")
        
    task = models.Task(**data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.get("", response_model = list[schemas.TaskOut])
def list_tasks(db:Session = Depends(get_db)):
    return db.query(models.Task).all()

@router.get("/{task_id}", response_model = schemas.TaskOut)
def get_task(task_id:int, db:Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code= 404, detail = "Task not found")
    return task

@router.patch("/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, data: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db:Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code = 404, detail = "Task not Found")
    db.delete(task)
    db.commit()
    return {"message": "deleted"}    
    


    