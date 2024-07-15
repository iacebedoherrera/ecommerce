import reflex as rx
from ecommerce.pages import index, my_account, products, product_view, shopping_cart
from ecommerce.api import api
import ecommerce.styles.styles as styles



class State(rx.State):
    pass

# Create app instance and add index page.
app = rx.App(
    style=styles.BASE_STYLE
)


# API USERS
app.api.add_api_route("/users/register", api.register_user)
app.api.add_api_route("/users/login", api.login_user, methods=["POST"])
app.api.add_api_route("/users/me", api.get_user)

#API PRODUCTS
app.api.add_api_route("/images/{product_type}/{partnumber}", api.get_product_images)
