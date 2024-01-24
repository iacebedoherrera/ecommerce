from rxconfig import config
import reflex as rx
from ecommerce.components.header import header


class State(rx.State):
    pass

@rx.page(route="/", title="I&N Shop")
def index() -> rx.Component:
    return header()


# Create app instance and add index page.
app = rx.App()
app.add_page(index)
