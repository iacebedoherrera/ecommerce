import reflex as rx
from ecommerce.pages import index, my_account, products, product_view, shopping_cart, confirm_order, shippings, returns, contact
from ecommerce.api import api
import ecommerce.styles.styles as styles



app = rx.App(
    style=styles.BASE_STYLE,
    theme=rx.theme(
        appearance="light",
        has_background=True
    )
)


# API USERS
app.api.add_api_route("/users/register", api.register_user)
app.api.add_api_route("/users/login", api.login_user, methods=["POST"])
app.api.add_api_route("/users/me", api.get_user)

# API PRODUCTS
app.api.add_api_route("/images/{product_type}/{partnumber}", api.get_product_images)

# PAYPAL
app.api.add_api_route("/order/checkout", api.create_order, methods=['POST'])
app.api.add_api_route("/orders/{order_id}/capture", api.capture_order, methods=['POST'])
app.api.add_api_route("/order/save", api.save_order, methods=['POST'])
