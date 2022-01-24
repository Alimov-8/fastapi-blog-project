from datetime import datetime, timedelta
from typing import Optional

from environs import Env
from jose import JWTError, jwt


# Environmental variables
env = Env()
env.read_env()


SECRET_KEY = env.str('SECRET_KEY')
ALGORITHM = env.str('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
