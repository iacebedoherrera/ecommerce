import reflex as rx
import os
import dotenv
from ecommerce.dal.dao.userDAO import UserDAO
from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from ecommerce.dal.models.user import User
from typing import Annotated
from ecommerce import const



dotenv.load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = const.ALGORITHM
ACCESS_TOKEN_DURATION = const.ACCESS_TOKEN_DURATION

oauth2 = OAuth2PasswordBearer(tokenUrl="/user/login")
crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



# Method that verifies if passwords in flat text and hashed coincided
def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)


# Method that applies a hash to the password
def get_password_hash(password):
    return crypt_context.hash(password)


# Method that authenticates the user
async def authenticate_user(email: str, password: str):
    user = UserDAO.find_user_by_email(email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


# Method that creates an access token
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Method that returns the current user through Token
async def get_current_user(token: Annotated[str, Depends(oauth2)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = UserDAO.find_user_by_email(username=email)
    if user is None:
        raise credentials_exception
    return user


# Method that checks if a user is disabled
async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# Method that returns access token
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> dict:
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_DURATION)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token":access_token, "token_type":"bearer"}


# Method that records a user in the system
def register_user(form_data: dict):
    user = User(**form_data)
    # We apply the hash to the password before saving it
    user.password = get_password_hash(user.password)
    UserDAO.insert(user)
