import reflex as rx
from sqlmodel import Field



class Product(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    partnumber: str
    family: int
    model: int
    color: str
    size: str
    price: float