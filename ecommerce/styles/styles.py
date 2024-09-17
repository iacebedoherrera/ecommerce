import reflex as rx
from enum import Enum
from .colors import Color

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
    ".carousel-container": {
        "position": "relative",
        "width": "100%",
        "max-width": "600px",
        "margin": "auto",
        "overflow": "hidden"
    },

    ".prev, .next": {
        "cursor": "pointer",
        "position": "absolute",
        "top": "50%",
        "transform": "translateY(-50%)",
        "padding": "10px",
        "color": "black",
        "font-weight": "bold",
        "font-size": "18px",
        "transition": "0.6s ease",
        "border-radius": "0 3px 3px 0",
        "z-index": "1"
    },

    ".next": {
        "right": "0"
    },

    ".prev": {
        "left": "0",
        "right": "auto"
    },

    ".mySlides": {
        "display": "none"
    },

    ".slideshow-container": {
        "position": "relative",
        "margin": "auto"
    }

}

BUTTON = {
    "width": "100%",
    "border_radius": Size.SMALL.value,
    "color": "#000000",
    "background_color": "#83d3f4",
    "white_space": "normal",
    "text_align": "start",
    "_hover": {
        "background_color": Color.SECONDARY.value
    }
}


