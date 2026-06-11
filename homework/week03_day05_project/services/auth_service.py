from datetime import datetime,timedelta
from jose import jwt 
SECRET_KEY = "your-secret-key"
ALGOITHM = "HS256"

def create_access_token(data:dict,expires_delta:timedelta = None):
    to_encode = daya.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedalta(minutes=15)

to_encode.update({"exp":expire})
encoded_jwt  = jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)
return encoded_jwt