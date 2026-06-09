from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate,UserResponse
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

router = APIRouter(prefix="/users",tags=["users"])

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(password:str,password_hash:str):
    return pwd_context.verify(password,password_hash)

@router.post("/register",response_model = UserResponse)
def register(user:UserCreate,db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400,detail="Username already registered")

    hashed_password = hash_password(user.password)
    db_user = User(username=user.username,password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

if __name__ == "__main__" :
    test_password = "123456"
    hashed = hash_password(test_password)
    print(f"原始密码:{test_password}")
    print(f"哈希结果:{hashed}")

    is_valid = verify_password("123456",hashed)
    print(f"验证正确密码:{is_valid}")

    is_valid= verify_password("wrong",hashed)
    print(f"验证错误密码:{is_valid}")