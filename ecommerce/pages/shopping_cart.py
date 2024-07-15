import reflex as rx
from ecommerce.components.header import header
from ecommerce.components.footer import footer
import ecommerce.utils as utils
from ecommerce.routes import Route
from ecommerce.state.shoppingState import ShoppingState
from typing import List
from ecommerce.state.shoppingState import ShoppingCartProduct



@rx.page(
    route=Route.SHOPPING_CART.value,
    title="Carrito",
    on_load=ShoppingState.load_shopping_cart
)
def shopping_cart() -> rx.Component:
    return rx.vstack(
        utils.lang(),
        header(),
        rx.divider(border_color="black"),
        rx.cond(
            ShoppingState.products_list.length() > 1,
            show_products_in_shopping_cart(),
            rx.text("Tu carrito aún está vacío. Corre a comprar!")
        ),
        footer()
    )


def show_products_in_shopping_cart() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Producto"),
                rx.table.column_header_cell("Precio unitario"),
                rx.table.column_header_cell("Cantidad"),
                rx.table.column_header_cell("Precio total artículo")
            )
        ),
        rx.table.body(
            rx.foreach(ShoppingState.products_list, show_product)
        )
    )


def show_product(product_view: list) -> rx.Component:
    return rx.table.row(
        rx.table.cell(product_view[0]),
        rx.table.cell(product_view[1]),
        rx.table.cell(product_view[2]),
        rx.table.cell(product_view[3])
    )