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
    images = []
    images.extend(["products/tshirt/010203/010203_01.jpg", "products/tshirt/010203/010203_02.jpg", 
                   "products/sweatshirt/020102/020102_01.jpg", "products/sweatshirt/020102/020102_02.jpg"])
    return rx.flex(
        rx.desktop_only(
            rx.flex(
                rx.grid(
                    rx.foreach(images, create_grid),
                    columns="2",
                    spacing="8",
                    align="center",
                    justify="center",
                    width="80%"
                ),
                align="center",
                justify="center"
            )
        ),
        rx.mobile_and_tablet(
            rx.center(
                rx.grid(
                    rx.foreach(images, create_grid),
                    columns="1",
                    spacing="0",
                    align="center",
                    justify="center",
                    width="80%"
                )
            )
        ),
        direction="column",
        align="center",
        justify="center",
        spacing="5",
        padding_bottom=Size.BIG.value
    )


def create_grid(image: str):
    return rx.flex(
        rx.image(src=image, width="500px", height="auto"),
        align="center"
    )