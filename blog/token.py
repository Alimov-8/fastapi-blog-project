from datetime import datetime, timedelta
from typing import Optional

from environs import Env
from jose import JWTError, jwt

from blog.database import get_db
from blog.schemas.token import TokenDataSchema

from blog.repository.users import get_user_by_email

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


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenDataSchema(email=email)
    except JWTError:
        raise credentials_exception

    db = get_db()
    user = get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception

    return user.first()
