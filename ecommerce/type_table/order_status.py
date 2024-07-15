from enum import Enum


class OrderStatus(Enum):
    CREATED = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4
