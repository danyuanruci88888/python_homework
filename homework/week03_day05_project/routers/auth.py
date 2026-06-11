from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import timedelta
from jose import JWTError,jwt
from database import User
from schemas import UserLogin,Token
from services.auth_service import create_access_token,SECRET_KEY,ALGORITHM
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
router = APIRouter(prefix="/auth",tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

@router.post("/login",response_model=Token)
def login(user_data:UserLogin,db:Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_data.username).first()

if not user or not verify_password(user_data.password,user.password_hash):
    raise HTTPException(status_code=401,detail="Incorrect username or password")

access_token = create_access_token(
    data = {"sub":str(user.id)},
    expires_delta = access_token_expires
)
return {"access_token":access_token,"token_type":"bearer"}

def get_current_user(token:str = Depends(oauth2_schme),db:Session = Depends(get_db)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZEO,
        detail="Could not vaildate credentials",
        headers={"WWW-Authenticate":"Bearer"},
    )

    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        user_id:str = payload.get