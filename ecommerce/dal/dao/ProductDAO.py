import reflex as rx
from ecommerce.dal.models.product import Product



class ProductDAO:

    # Find a product from the partnumber
    def find_by_partnumber(partnumber: str):
        with rx.session() as session:
            return session.exec(Product.select().where(Product.partnumber == partnumber)).first()
        

    # Find a product from the id
    def find_by_id(id: int):
        with rx.session() as session:
            return session.exec(Product.select().where(Product.id == id)).first()