import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "560px"


# Sizes

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    ULTRA_BIG = "20em"


# Styles
BASE_STYLE = {
    rx.divider: {
        "color_scheme": "mint"
    }
}

BUTTON = {
    "width": "100%",
    "height": "100%",
    "padding": Size.SMALL.value,
    "border_radius": Size.SMALL.value,
    "color": "#000000",
    "background_color": "#83d3f4",
    "white_space": "normal",
    "text_align": "start",
    "_hover": {
        "background_color": Color.SECONDARY.value
    }
}


