import reflex as rx
from sqlmodel import Field



class Product(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    partnumber: str
    family: str
    model: str
    color: str
    size: str
    price: str