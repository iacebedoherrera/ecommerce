import reflex as rx
from ecommerce.components.header import header
from ecommerce.components.footer import footer
from ecommerce.routes import Route
import ecommerce.utils as utils
from ecommerce.styles.styles import Size

@rx.page(
    route=Route.INDEX.value, 
    title="INUsual"
)
def index() -> rx.Component:
    return rx.flex(
        utils.lang(),
        header(),
        products_index(),
        footer(),
        direction="column",
        spacing="5",
        position="relative",
        min_height="100vh"
    )


def products_index() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.link(
                rx.image(
                    src="/icons/men.avif",
                    height=Size.ULTRA_BIG.value
                )
            )
        ),
        rx.vstack(
            rx.link(
                rx.image(
                    src="/icons/women.avif",
                    height=Size.ULTRA_BIG.value
                )
            )
        ),
        direction="row",
        justify="center",
        spacing="5",
        padding_bottom=Size.BIG.value
    )


