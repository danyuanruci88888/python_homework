import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate, UserResponse
from routers.auth import get_current_user
from passlib.context import CryptContext

logger = logging.getLogger(__name__)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter(prefix="/users", tags=["users"])


def hash_password(password: str):
    return pwd_context.hash(password)


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        logger.warning(f"用户名 {user.username} 已存在")
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = hash_password(user.password)
    db_user = User(username=user.username, password_hash=hashed_password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    logger.info(f"用户 {user.username} 注册成功")
    return db_user


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    logger.info(f"获取当前用户信息: {current_user.username}")
    return current_user
