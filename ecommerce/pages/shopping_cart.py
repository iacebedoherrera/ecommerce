import reflex as rx
import os, dotenv
from ecommerce.components.header import header
from ecommerce.components.footer import footer
import ecommerce.utils as utils
from ecommerce.routes import Route
from ecommerce.state.shoppingState import ShoppingState
from ecommerce.state.userState import LoginState
from ecommerce.styles.styles import Size


dotenv.load_dotenv()


@rx.page(
    route=Route.SHOPPING_CART.value,
    title="Carrito",
    on_load=[ShoppingState.load_shopping_cart, ShoppingState.save_paypal_data, LoginState.verify_pay]
)
def shopping_cart() -> rx.Component:
    return rx.flex(
        utils.lang(),
        header(),
        rx.cond(
            ShoppingState.products_list.length() > 1,
            show_checkout(),
            show_go_shopping()
        ),
        rx.dialog.root(
            rx.dialog.content(
                rx.flex(
                    rx.center(
                        rx.dialog.title(
                            rx.icon("shirt", color="red", size=100)
                        )
                    ),
                    rx.text("No hay stock de este artículo. Pruebe en otro momento."),
                    rx.dialog.close(
                        rx.flex(
                            rx.button("Cerrar", color_scheme="red", on_click=ShoppingState.change_no_stock_message),
                            direction="column"
                        )
                    ),
                    direction="column",
                    align="center",
                    spacing="3"
                ),
            ),
            open=ShoppingState.show_no_stock_message
        ),
        footer(),
        direction="column",
        position="relative",
        min_height="100vh"
    )

def show_go_shopping() -> rx.Component:
    return rx.flex(
        rx.icon("shopping-bag", size=150),
        rx.text("Tu carrito aún está vacío. ¡Corre a comprar!"),
        direction="column",
        align="center",
        spacing="7",
        padding_bottom=Size.BIG.value
    )

def show_checkout() -> rx.Component:
    return rx.flex(
        show_products_in_shopping_cart(),
        rx.cond(
            LoginState.login_cookie is not None and LoginState.login_cookie != "",
            rx.cond(
                #LoginState.get_user_address() is None or LoginState.get_user_phone() == "",
                LoginState.can_pay,
                show_payment(),
                show_review_user_data()
            ),
            rx.text("Debes iniciar sesión para poder realizar tu compra")
        ),
        direction="column",
        align="center",
        spacing="8",
        padding_bottom=Size.BIG.value
    )

def show_products_in_shopping_cart() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Producto"),
                rx.table.column_header_cell("Talla"),
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
        rx.table.cell(
            rx.cond(
                product_view[0] != "PRECIO TOTAL",
                rx.flex(
                    rx.icon("circle-minus", on_click=ShoppingState.update_product_qty(product_view[0], product_view[1], -1)),
                    product_view[3],
                    rx.icon("circle-plus", on_click=ShoppingState.update_product_qty(product_view[0], product_view[1], 1)),
                    direction="row",
                    spacing="2"
                )
            )
        ),
        rx.table.cell(product_view[4])
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
            )
        )
    )


def show_review_user_data() -> rx.Component:
    return rx.flex(
        rx.text("Tienes que completar todos los datos de usuario antes de finalizar con el pago."),
        rx.button(
            "Mis datos",
            width="50%",
            on_click=rx.redirect(Route.MY_ACCOUNT.value)
        ),
        direction="column",
        align="center",
        spacing="4"
    )