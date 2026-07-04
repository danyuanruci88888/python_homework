from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Favorite,User,Job
from schemas import FavoriteCreate,FavoriteResponse
from routers.auth import get_current_user

router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.post("/", response_model=FavoriteResponse)
def add_favorite(
    favorite: FavoriteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    job = db.query(Job).filter(Job.id == favorite.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    existing = db.query(Favorite).filter(
        Favorite.user_id == current_user.id,
        Favorite.job_id == favorite.job_id
    ).first()
    if existing:
        raise HTTPException(status_code=400,detail="Already favorited")

    db_favorite = Favorite(user_id=current_user.id, job_id=favorite.job_id)
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite

@router.get("/", response_model=list[FavoriteResponse])
def get_my_favorites(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Favorite).filter(Favorite.user_id == current_user.id).all()