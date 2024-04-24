import reflex as rx
from ecommerce.components.header import header
from ecommerce.components.footer import footer
from ecommerce.components.products_index import products_index
from ecommerce.routes import Route
import ecommerce.utils as utils

@rx.page(
    route=Route.INDEX.value, 
    title="I&N Shop"
)
def index() -> rx.Component:
    return rx.vstack(
        utils.lang(),
        header(),
        rx.divider(border_color="black"),
        products_index(),
        #social_media(),
        footer()
    )


