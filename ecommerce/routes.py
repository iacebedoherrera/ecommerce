from enum import Enum


class Route(Enum):
    INDEX = "/"
    MY_ACCOUNT = "/my_account"
    PRODUCTS = "/products"
    SHOPPING_CART = "/shopping_cart"
    CONFIRM_ORDER = "/order_confirm"
    SHIPPINGS = "/shippings"
    RETURNS = "/returns"
    CONTACT = "/contact"

    PAYPAL = "https://www.paypal.com/es/home"
    REFLEX = "https://reflex.dev/"