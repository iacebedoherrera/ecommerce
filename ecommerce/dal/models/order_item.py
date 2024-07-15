import reflex as rx
from sqlmodel import Field
from datetime import datetime



class OrderItem(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)
    order_id: int
    sku: str
    quantity: int
    creation_date: datetime = Field(default_factory=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))