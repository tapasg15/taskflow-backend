from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix = "/users", tags = ["Users"])

@router.post("", response_model = schemas.UserOut)
def create_user(data: schemas.UserCreate, db:Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == data.email).first()
    if existing:
        raise HTTPException(status_code = 404, detail = "Email already registered")
    
    user = models.User(
        name=data.name,
        email=data.email,
        password_hash=data.password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("", response_model =list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

