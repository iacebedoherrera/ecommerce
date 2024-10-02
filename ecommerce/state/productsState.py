import reflex as rx
import os
import ecommerce.const as const
from ecommerce.api.ProductAPI import ProductAPI
from typing import List
from ecommerce.dal.models.product import Product




PRODUCT_API = ProductAPI()


class ProductAttributes(rx.Base):
    product_path: str
    product_name: str
    product: Product

class ProductsState(rx.State):
    products: List[ProductAttributes] = []
    page_loading: bool = True

    @rx.var
    def get_product_type(self) -> str:
        return self.router.page.params.get("product_type", "")

    def change_page_loading(self, value: bool):
        self.page_loading = value
    
    async def update_products(self):
        product_type: str = self.get_product_type
        route: str = "assets/products/" + product_type
        product_list: List[ProductAttributes] = []
        for filename in os.listdir(route):
            try:
                product: Product = await PRODUCT_API.get_product_by_partnumber(filename + "01")
                product_path = os.path.join('/products', product_type, filename, filename) + "_01" + const.IMAGES_FORMAT
                product_attributes: ProductAttributes = ProductAttributes(product_path=product_path, product_name=filename, product=product)
                product_list.append(product_attributes)
            except:
                continue
        self.products = product_list

    def update_page_name(self):
        title = const.PRODUCTS.get(self.get_product_type)
        self.page_loading = False
        return rx.call_script(f"document.title = '{title}';")