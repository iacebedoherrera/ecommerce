import reflex as rx
from sqlmodel import Field



class Stock(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)
    partnumber: str = Field(unique=True)
    quantity: int