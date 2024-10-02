import reflex as rx
from ecommerce.dal.models.product import Product
from ecommerce.dal.models.product_stock import Stock



class ProductDAO:

    # Find a product from the partnumber
    def find_by_partnumber(partnumber: str):
        with rx.session() as session:
            return session.exec(Product.select().where(Product.partnumber == partnumber)).first()
        

    # Find a product from the id
    def find_by_id(id: int):
        with rx.session() as session:
            return session.exec(Product.select().where(Product.id == id)).first()
        
    
    # Returns the quantity of a product
    def get_quantity_by_partnumber(partnumber: str):
        with rx.session() as session:
            product_stock: Stock = session.exec(Stock.select().where(Stock.partnumber == partnumber)).first()
            if product_stock:
                return product_stock.quantity
            else:
                return None
            
    
    def update_quantity_by_product_id(partnumber: str, quantity_variation: float):
        with rx.session() as session:
            product_stock: Stock = session.exec(Stock.select().where(Stock.partnumber == partnumber)).first()
            if product_stock:
                product_stock.quantity = product_stock.quantity + quantity_variation
                session.commit()
            else:
                raise Exception("No se encuentra el stock del articulo.")