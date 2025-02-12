import reflex as rx
from ecommerce.components.header import header
from ecommerce.components.footer import footer
from ecommerce.routes import Route
import ecommerce.utils as utils
from rx_carousel.carousel import carousel

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
    images.extend(["products/tshirt/010101/010101_01.jpg", "products/tshirt/010203/010203_01.jpg", 
                   "products/tshirt/010302/010302_01.jpg", "products/tshirt/010401/010401_01.jpg",
                   "products/sweatshirt/020102/020102_01.jpg", "products/sweatshirt/020202/020202_01.jpg",
                   "products/sweatshirt/020302/020302_01.jpg", "products/sweatshirt/020402/020402_01.jpg"])
    
    return rx.flex(
        carousel(
            rx.foreach(images, create_image_carousel),
            autoPlay=True,
            interval=3000,
            infiniteLoop=True,
            showThumbs=False, 
            showStatus=False,
            stopOnHover=True,
            showArrows=False,
            width="80vw",
            max_width="700px",
            height="auto"
        ),
        rx.flex(
            rx.center(
                rx.flex(
                    rx.image(src="icons/+destacado.png"),
                    direction="column",
                    align="center",
                    width="80%"
                ),
            ),
            rx.desktop_only(
                rx.center(
                    rx.flex(
                        rx.image(src="icons/tshirt_index.jpg", on_click=rx.redirect(f"{Route.PRODUCTS.value}/tshirt")),
                        rx.image(src="icons/sweatshirt_index.jpg", on_click=rx.redirect(f"{Route.PRODUCTS.value}/sweatshirt")),
                        direction="row",
                        wrap="wrap",
                        align="center",
                        justify="center",
                        spacing="6",
                        width="90%",
                        height="auto"
                    ),
                )
            ),
            rx.mobile_and_tablet(
                rx.center(
                    rx.flex(
                        rx.image(src="icons/tshirt_index.jpg", on_click=rx.redirect(f"{Route.PRODUCTS.value}/tshirt")),
                        rx.image(src="icons/sweatshirt_index.jpg", on_click=rx.redirect(f"{Route.PRODUCTS.value}/sweatshirt")),
                        direction="column",
                        align="center",
                        justify="center",
                        spacing="6",
                        width="80vw",
                        height="auto"
                    ),
                )
            ),
            direction="column",
            spacing="5"
        ),
        direction="column",
        spacing="9",
        align="center",
        width="100%"
    )


def create_image_carousel(image_path: str):
    return rx.image(
        src=image_path
    )