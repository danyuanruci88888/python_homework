from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Application, User,Job
from schemas import ApplicationCreate, ApplicationUpdate,ApplicationResponse
from routers.auth import get_current_user

router = APIRouter(prefix="/applications", tags=["applications"])

@router.post("/", response_model=ApplicationResponse)
def create_application(
        app: ApplicationCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    job = db.query(Job).filter(Job.id == app.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    db_application = Application(
        user_id=current_user.id,
        job_id=app.job_id,
        notes=app.notes
    )
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

@router.get("/", response_model=list[ApplicationResponse])
def get_my_applications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Application).filter(Application.user_id == current_user.id).all()

@router.put("/{application_id}", response_model=ApplicationResponse)
def update_application(
    application_id:int,
    app: ApplicationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_application = db.query(Application).filter(
        Application.id == application_id,
        Application.user_id == current_user.id
    ).first()

    if not db_application:
        raise HTTPException(status_code=404,detail="Application not found")

    db_application.status = app.status
    if app.notes is not None:
        db_application.notes = app.notes
    
    db.commit()
    db.refresh(db_application)
    return db_application