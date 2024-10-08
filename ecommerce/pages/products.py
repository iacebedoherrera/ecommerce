import reflex as rx
from ecommerce.routes import Route
import ecommerce.utils as utils
from ecommerce.components.header import header
from ecommerce.components.footer import footer
from ecommerce.styles.styles import Size
from ecommerce.state.productsState import ProductsState, ProductAttributes
from ecommerce.pages.product_view import ProductState


        

@rx.page(
    route=f"{Route.PRODUCTS.value}/[product_type]",
    title="Productos",
    on_load=[ProductsState.update_products, ProductsState.update_page_name]
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
        rx.desktop_only(
            rx.flex(
                rx.grid(
                    rx.foreach(ProductsState.products, create_product_view),
                    columns="2",
                    spacing="8",
                    width="95%"
                ),
                align="center",
                justify="center"
            ),
        ),
        rx.mobile_and_tablet(
            rx.flex(
                rx.grid(
                    rx.foreach(ProductsState.products, create_product_view),
                    columns="1",
                    spacing="6",
                    width="80%"
                ),
                align="center",
                justify="center"
            ),
        ),
        direction="column",
        align="center",
        width="100%",
        padding_bottom=Size.BIG.value
    )


def create_product_view(product: ProductAttributes):
    return rx.skeleton(
        rx.flex(
            rx.link(
                rx.image(src=product.product_path),
                href=Route.PRODUCTS.value + "/" + ProductsState.get_product_type + "/" + product.product.partnumber[:-2],
                on_click=ProductState.change_page_loading(True)
            ),
            rx.flex(
                rx.text(product.product.name),
                rx.text(product.product.price + " €"),
                direction="column",
                align="center"
            ),
            spacing="2",
            direction="column",
            align="center"
        ),
        loading=ProductsState.page_loading
    )

