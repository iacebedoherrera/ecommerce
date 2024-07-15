import reflex as rx
from sqlmodel import Field
from datetime import datetime



class Order(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int
    address_id: int
    creation_date: datetime = Field(default_factory=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    status_id: int