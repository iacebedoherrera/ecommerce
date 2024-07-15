import reflex as rx
from ecommerce.dal.models.order import Order


class OrderDAO:

    # Insert a new order
    def insert(order: Order) -> int:
        with rx.session() as session:
            session.add(order)
            session.commit()
            session.refresh(order)
            return order.id

    # Find a order from id
    def find_order_by_id(id: int):
        with rx.session() as session:
            return session.exec(Order.select().where(Order.id == id)).first()


    # Find all users
    def find_all_orders():
        with rx.session() as session:
            return session.exec(Order).all()
