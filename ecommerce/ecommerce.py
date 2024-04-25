import reflex as rx
from ecommerce.pages.index import index
from ecommerce.api.userAPI import register_user, login_for_access_token

class State(rx.State):
    pass

# Create app instance and add index page.
app = rx.App()

# API Usuarios
app.api.add_api_route("/users/register", register_user)
#app.api.add_api_route("/users/login", login_for_access_token)
