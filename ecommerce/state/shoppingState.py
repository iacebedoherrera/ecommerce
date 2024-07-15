import reflex as rx
from ecommerce.dal.models.product import Product
from ecommerce.api.ProductAPI import ProductAPI
from ecommerce.type_table.product_family import Family
from typing import List


PRODUCT_API = ProductAPI()


class ShoppingCartProduct(rx.Base):
    product: Product = Product()
    quantity: int


# Class that manages the shopping cart
class ShoppingState(rx.State):
    products: dict[int, ShoppingCartProduct] = {}
    products_list: list[list] = []

    async def add_product_to_shopping_cart(self, id: int):
        product: Product = await PRODUCT_API.get_product_by_id(id)
        if self.products.get(product.id):
            self.products.get(product.id).quantity += 1
        else:
            shopping_cart_product: ShoppingCartProduct = ShoppingCartProduct(product=product, quantity=1)
            self.products[product.id] = shopping_cart_product
        
    def create_path_for_image(self, shoppingCartProduct: ShoppingCartProduct) -> str:
        product: Product = shoppingCartProduct.product
        path: str = "/products/" + Family.get_family(product.id) + "/" + product.partnumber + "/" + product.partnumber + "_01.jpg"
        print(path)
        return path
    
    def load_shopping_cart(self):
        products_list: list[list] = []
        total_amount: float = 0.0
        for shoppingCartProduct in self.products.values():
            product: list = []
            product.append(shoppingCartProduct.product.name)
            total_amount += shoppingCartProduct.product.price
            product.append(f"{shoppingCartProduct.product.price}€")
            product.append(shoppingCartProduct.quantity)
            product.append(f"{float(shoppingCartProduct.product.price) * shoppingCartProduct.quantity}€")
            products_list.append(product)

        total_amount_row: list = []
        total_amount_row.append("PRECIO TOTAL")
        total_amount_row.append("")
        total_amount_row.append("")
        total_amount_row.append(f"{float(total_amount)}€")
        products_list.append(total_amount_row)

        self.products_list = products_list


    