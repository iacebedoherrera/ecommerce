import reflex as rx
import os
from ecommerce.routes import Route
import ecommerce.const as const
import ecommerce.utils as utils
from ecommerce.components.header import header
from ecommerce.components.footer import footer
from ecommerce.api.ProductAPI import ProductAPI
from typing import List
from ecommerce.dal.models.product import Product
from ecommerce.styles.styles import Size


PRODUCT_API = ProductAPI()


class ProductAttributes(rx.Base):
    product_path: str
    product_name: str
    product: Product

class ProductsState(rx.State):
    products: List[ProductAttributes] = []

    @rx.var
    def get_product_type(self) -> str:
        return self.router.page.params.get("product_type", "")
    
    async def update_products(self):
        if not self.products:
            product_type: str = self.get_product_type
            route: str = "assets/products/" + product_type
            product_list: List[ProductAttributes] = []
            for filename in os.listdir(route):
                try:
                    product: Product = await PRODUCT_API.get_product_by_partnumber(filename)
                except:
                    continue
                product_path = os.path.join('/products', product_type, filename, filename) + "_01" + const.IMAGES_FORMAT
                product_attributes: ProductAttributes = ProductAttributes(product_path=product_path, product_name=filename, product=product)
                product_list.append(product_attributes)
            self.products = product_list

        

@rx.page(
    route=f"{Route.PRODUCTS.value}/[product_type]",
    title=const.PRODUCTS.get(ProductsState.get_product_type),
    on_load=ProductsState.update_products
)
def products() -> rx.Component:
    return rx.flex(
        utils.lang(),
        header(),
        product_list(),
        footer(),
        direction="column",
        position="relative",
        min_height="100vh"
    )


def product_list() -> rx.Component:
    return rx.flex(
        rx.grid(
            rx.foreach(ProductsState.products, create_product_view),
            columns="2",
            spacing="8",
            width="80%"
        ),
        direction="column",
        align="center",
        width="100%",
        padding_bottom=Size.BIG.value
    )


def create_product_view(product: ProductAttributes):
    return rx.flex(
        rx.link(
            rx.image(src=product.product_path, width="300px", height="auto"),
            href=Route.PRODUCTS.value + "/" + ProductsState.get_product_type + "/" + product.product.partnumber
        ),
        rx.text(product.product.name),
        rx.text(product.product.price + " €"),
        direction="column",
        align="center"
    )

