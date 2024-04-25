import reflex as rx
from ecommerce.pages import index, my_account, products
from ecommerce.api import api
import ecommerce.styles.styles as styles



class State(rx.State):
    pass

# Create app instance and add index page.
app = rx.App(
    style=styles.BASE_STYLE
)


# API Usuarios
app.api.add_api_route("/users/register", api.register_user)
app.api.add_api_route("/users/login", api.login_user, methods=["POST"])
app.api.add_api_route("/users/me", api.get_user)
