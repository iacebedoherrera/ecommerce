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
        product_partnumbers: List[str] = []
        for filename in os.listdir(route):
            product_partnumbers.append(filename + "01")
        product_list_from_db: List[Product] = await PRODUCT_API.get_products_by_partnumbers(product_partnumbers)
        for product in product_list_from_db:
            try:
                product_path = os.path.join('/products', product_type, product.partnumber[:-2], product.partnumber[:-2]) + "_01" + const.IMAGES_FORMAT
                product_attributes: ProductAttributes = ProductAttributes(product_path=product_path, product_name=product.partnumber[:-2], product=product)
                product_list.append(product_attributes)
            except:
                continue
        self.products = product_list

    def update_page_name(self):
        title = const.PRODUCTS.get(self.get_product_type)
        self.page_loading = False
        return rx.call_script(f"document.title = '{title}';")