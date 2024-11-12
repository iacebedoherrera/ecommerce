import reflex as rx
from ecommerce.routes import Route
import ecommerce.const as const
import ecommerce.utils as utils
from ecommerce.components.header import header
from ecommerce.components.footer import footer
from ecommerce.state.shoppingState import ShoppingState
from ecommerce.styles.styles import Size
from ecommerce.state.confirmOrderState import ConfirmOrderState



@rx.page(
    route=f"{Route.CONFIRM_ORDER.value}/[order_id]",
    title=const.ORDER_CONFIRM,
    on_load=ShoppingState.clean_shopping_cart
)
def confirm_order() -> rx.Component:
    return rx.flex(
        utils.lang(),
        header(),
        confirm(),
        footer(),
        direction="column",
        position="relative",
        min_height="100vh"
    )


def confirm() -> rx.Component:
    return rx.flex(
        rx.icon("circle-check-big", color="green", size=150),
        rx.text(
            "¡Enhorabuena! Has realizado tu compra con éxito"
        ),
        rx.text(
            f"Tu código de pedido es: {ConfirmOrderState.order_id}"
        ),
        direction="column",
        align="center",
        spacing="4",
        width="100%",
        padding_bottom=Size.BIG.value
    )