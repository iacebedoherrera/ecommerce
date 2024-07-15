import reflex as rx
import os, dotenv
from ecommerce.components.header import header
from ecommerce.components.footer import footer
import ecommerce.utils as utils
from ecommerce.routes import Route
from ecommerce.state.shoppingState import ShoppingState
from ecommerce.state.userState import LoginState


dotenv.load_dotenv()
BACKEND_URL = os.environ.get("BACKEND_URL")


@rx.page(
    route=Route.SHOPPING_CART.value,
    title="Carrito",
    on_load=[ShoppingState.load_shopping_cart, ShoppingState.save_paypal_data]
)
def shopping_cart() -> rx.Component:
    return rx.vstack(
        utils.lang(),
        header(),
        rx.divider(border_color="black"),
        rx.cond(
            ShoppingState.products_list.length() > 1,
            show_checkout(),
            rx.text("Tu carrito aún está vacío. Corre a comprar!")
        ),
        footer() 
    )

def show_checkout() -> rx.Component:
    return rx.hstack(
        show_products_in_shopping_cart(),
        rx.cond(
            LoginState.login_cookie is not None and LoginState.login_cookie != "",
            show_payment(),
            rx.text("Debes iniciar sesión para poder realizar tu compra")
        )
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
        rx.table.cell(
            rx.cond(
                product_view[0] != "PRECIO TOTAL",
                rx.flex(
                    rx.icon("circle-minus", on_click=ShoppingState.update_product_qty(product_view[0], -1)),
                    product_view[2],
                    rx.icon("circle-plus", on_click=ShoppingState.update_product_qty(product_view[0], 1)),
                    direction="row"
                )
            )
        ),
        rx.table.cell(product_view[3])
    )

def show_payment() -> rx.Component:
    return rx.vstack(
        rx.html(
            "",
            id="paypal-button-container"
        ),
        rx.script(
            src="/javascript/paypal.js"
        ),
        rx.script(
            src="https://www.paypal.com/sdk/js?client-id=ATN9EHN2s7Qz0o_TpmYzrEJU39p4IIH6XDDQyH_XbOxN5mQKhDeDvzrEj9rorcLy7AIRoitgJuB8AumU&currency=EUR",
            custom_attrs={"data-sdk-integration-source": "developer-studio"},
            on_ready=rx.call_script(
                "paypalButton();",
                #callback=ShoppingState.get_order_result
            )
        )
    )