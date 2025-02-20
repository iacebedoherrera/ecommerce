from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import random
import smtplib
import string
import dotenv
from ecommerce.dal.dao.UserDAO import UserDAO
from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from ecommerce.dal.models.user import User
from typing import Annotated
from ecommerce import const
from ecommerce.api import api
from ecommerce.service.emailService import EmailService



class UserAPI:
    dotenv.load_dotenv()

    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = const.ALGORITHM
    ACCESS_TOKEN_DURATION = const.ACCESS_TOKEN_DURATION

    oauth2 = OAuth2PasswordBearer(tokenUrl="/users/login")
    crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


    # Method that verifies if passwords in flat text and hashed coincided
    def verify_password(self, plain_password, hashed_password):
        return self.crypt_context.verify(plain_password, hashed_password)


    # Method that applies a hash to the password
    def get_password_hash(self, password):
        return self.crypt_context.hash(password)


    # Method that authenticates the user
    async def authenticate_user(self, email: str, password: str):
        user: User = UserDAO.find_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="The user does not exist",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if password == user.password:
            return user
        if not self.verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The password is not correct",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user


    # Method that creates an access token
    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt


    # Method that returns the current user through Token
    async def get_current_user(self, token: Annotated[str, Depends(oauth2)]):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                raise self.credentials_exception
        except JWTError:
            raise self.credentials_exception
        user: User = UserDAO.find_user_by_email(email=email)
        if user is None:
            raise self.credentials_exception
        return user


    # Method that returns access token
    async def login_for_access_token(self,
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    ) -> dict:
        user = await self.authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=self.ACCESS_TOKEN_DURATION)
        access_token = self.create_access_token(
            data={"sub": user.email, "token_type": "bearer"}, 
            expires_delta=access_token_expires
        )
        return {"access_token":access_token, "username":user.name}


    # Method that records a user in the system
    def register_user(self, user: User):
        # We apply the hash to the password before saving it
        if user.password is not None:
            user.password = self.get_password_hash(user.password)
        try:
            return UserDAO.insert(user)
        except:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="The user already exists in the system",
                headers={"WWW-Authenticate": "Bearer"},
            )


    # Method that allows a user to recover his password
    async def recover_password(self, email: str):
        password = self.generate_password(12)
        mensaje = (f"Esta es tu nueva contraseña: {password}")
        try:
            user: User = UserDAO.find_user_by_email(email)
            password_dict = {"password": password}
            await api.update_user(user.id, password_dict)
        except:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Can't reset password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        await EmailService.sendEmail(email, "Recuperar contraseña", mensaje)

    
    # Method that creates a secure password
    def generate_password(self, long: int):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(long))
        return password

