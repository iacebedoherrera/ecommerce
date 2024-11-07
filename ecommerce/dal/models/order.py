import reflex as rx
from sqlmodel import Field, Relationship
from datetime import datetime
from typing import List



class Order(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int
    address_id: int
    creation_date: datetime = Field(default_factory=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    status_id: int
    order_items: List["OrderItem"] = Relationship(back_populates="order")



class OrderItem(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)
    order_id: int = Field(default=None, foreign_key="order.id")
    partnumber: str
    quantity: int
    creation_date: datetime = Field(default_factory=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    order: Order = Relationship(back_populates="order_items")