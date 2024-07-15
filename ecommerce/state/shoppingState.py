import reflex as rx
import json
from ecommerce.dal.models.product import Product
from ecommerce.api.ProductAPI import ProductAPI
from ecommerce.type_table.product_family import Family
from ecommerce.routes import Route


PRODUCT_API = ProductAPI()


class ShoppingCartProduct(rx.Base):
    product: Product = Product()
    quantity: int

class ShoppingDataPaypal(rx.Base):
    products: dict = {}
    total_amount = 0.0


# Class that manages the shopping cart
class ShoppingState(rx.State):
    products: dict[int, ShoppingCartProduct] = {}
    products_list: list[list] = []
    total_amount = 0.0
    paypal_products: str = rx.LocalStorage(name="products")
    paypal_amount: str = rx.LocalStorage(name="amount")

    async def add_product_to_shopping_cart(self, id: int):
        product: Product = await PRODUCT_API.get_product_by_id(id)
        if self.products.get(product.id):
            self.products.get(product.id).quantity += 1
        else:
            shopping_cart_product: ShoppingCartProduct = ShoppingCartProduct(product=product, quantity=1)
            self.products[product.id] = shopping_cart_product
        self.total_amount += product.price
        
    def create_path_for_image(self, shoppingCartProduct: ShoppingCartProduct) -> str:
        product: Product = shoppingCartProduct.product
        path: str = "/products/" + Family.get_family(product.id) + "/" + product.partnumber + "/" + product.partnumber + "_01.jpg"
        return path
    
    def load_shopping_cart(self):
        products_list: list[list] = []
        for shoppingCartProduct in self.products.values():
            product: list = []
            product.append(shoppingCartProduct.product.name)
            product.append(f"{shoppingCartProduct.product.price}€")
            product.append(shoppingCartProduct.quantity)
            product.append(f"{float(shoppingCartProduct.product.price) * shoppingCartProduct.quantity}€")
            products_list.append(product)

        total_amount_row: list = []
        total_amount_row.append("PRECIO TOTAL")
        total_amount_row.append("")
        total_amount_row.append("")
        total_amount_row.append(f"{float(self.total_amount)}€")
        products_list.append(total_amount_row)

        self.products_list = products_list

    def save_paypal_data(self):
        products = {}
        for shoppingCartProduct in self.products.values():
            products[shoppingCartProduct.product.partnumber] = shoppingCartProduct.quantity

        self.paypal_products = json.dumps(products)
        self.paypal_amount = self.total_amount

    def update_product_qty(self, product_name: str, updated_qty: int):
        for id in self.products.keys():
            product = self.products.get(id)
            if product.product.name == product_name:
                if updated_qty > 0:
                    self.total_amount += product.product.price
                    product.quantity += updated_qty
                else:
                    if product.quantity != 0:
                        self.total_amount -= product.product.price
                        product.quantity += updated_qty
                        if product.quantity == 0:
                            self.products.pop(id)
                break

        for product in self.products_list:
            if product[2] == product_name:
                product[2] += updated_qty
                if product[2] == 0:
                    index = self.products_list.index(product)
                    self.products_list.pop(index)
                break
        
        self.save_paypal_data()
        return rx.redirect(Route.SHOPPING_CART.value)
    
    def clean_shopping_cart(self):
        self.products.clear()
        self.products_list.clear()
        self.total_amount = 0.0

    
    
    
