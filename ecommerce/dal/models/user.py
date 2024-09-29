import reflex as rx
from sqlmodel import Field, Relationship
from typing import Optional, List


class Address(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)
    address: str
    city: str
    autonomous_community: str
    postal_code: str
    users: List["User"] = Relationship(back_populates="address")

    
    def __str__(self):
        return (
            f"{self.address}, \n"
            f"{self.city}, \n"
            f"{self.autonomous_community}, \n"
            f"{self.postal_code}"
        )
    

class User(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    surname: str
    email: str = Field(unique=True)
    password: Optional[str]
    phone_number: str
    disabled: bool = Field(default=False)
    address_id: Optional[int] = Field(default=None, foreign_key="address.id")
    address: Optional[Address] = Relationship(back_populates="users")
    is_google_user: bool

