import reflex as rx
from sqlmodel import Field
from typing import Optional

class User(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    surname: str
    email: str = Field(unique=True)
    password: str
    address_id: Optional[int] = Field(default=None)
    phone_number: str
    disabled: bool = Field(default=False)