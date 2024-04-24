import reflex as rx
import os
from urllib.parse import urlparse
from ecommerce.routes import Route
import ecommerce.const as const
import ecommerce.utils as utils
from ecommerce.components.header import header
from ecommerce.components.footer import footer
from ecommerce.dal.models.product import Product
from ecommerce.dal.dao.ProductDAO import ProductDAO
from ecommerce.api.ProductAPI import ProductAPI


PRODUCT_API = ProductAPI()


class ProductAttributes(rx.Base):
    product_path: str
    product_name: str
    product: Product

class ProductState(rx.State):
    products: list[ProductAttributes] = []
    current_product: Product = Product()

    @rx.var
    def product_type(self) -> str:
        return self.router.page.params.get("product_type", "")
    
    async def update_products(self):
        product_type: str = self.router.page.params.get("product_type", ".")
        route: str = "assets/products/" + product_type
        product_list: list[ProductAttributes] = []
        for filename in os.listdir(route):
            try:
                product: Product = await PRODUCT_API.get_product_by_partnumber(filename)
            except:
                continue
            new_route: ProductAttributes = ProductAttributes(product_path=os.path.join(product_type, filename), product_name=filename, product=product)
            product_list.append(new_route)
        self.products = product_list
        

@rx.page(
    route=f"{Route.PRODUCTS.value}/[product_type]",
    title=const.PRODUCTS.get(ProductState.product_type),
    on_load=ProductState.update_products
)
def products() -> rx.Component:
    return rx.vstack(
        utils.lang(),
        header(),
        rx.divider(border_color="black"),
        product_list(),
        footer()
    )


def product_list() -> rx.Component:
    return rx.vstack(
        rx.foreach(ProductState.products, create_product_view)
    )


def create_product_view(product: ProductAttributes):
    return rx.vstack(
        rx.image(product.product_path),
        rx.text(product.product_name),
        rx.text(product.product.price)
    )

