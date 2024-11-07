import reflex as rx
from ecommerce.dal.models.order import OrderItem


class OrderItemDAO:

    # Insert a new order
    def insert(order_item: OrderItem) -> int:
        with rx.session() as session:
            session.add(order_item)
            session.commit()
            session.refresh(order_item)
            return order_item.id

    # Find a order from id
    def find_order_item_by_id(id: int):
        with rx.session() as session:
            return session.exec(OrderItem.select().where(OrderItem.id == id)).first()


    # Find all users
    def find_all_orders():
        with rx.session() as session:
            return session.exec(OrderItem).all()