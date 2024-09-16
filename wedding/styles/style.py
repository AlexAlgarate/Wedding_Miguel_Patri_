from enum import Enum

import reflex as rx

from wedding.styles.colors import Color
from wedding.styles.fonts import Font, FontWeight

# Constants
MAX_WIDTH = "800px"
FLEX_DIRECTION = ["column", "column", "column", "row", "row"]

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Antic+Didone&family=Alex+Brush&family=Elsie&family=Raleway&display=swap",
    "/styles.css",
]


# Styles
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.25em"
    MEDIUM_SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    MAIN_TEXTS = "1.15em"
    LARGE = "1.5em"
    BIG = "2em"
    BIG_TITLES = "2.5em"
    MEDIUM_BIGGER = "3em"
    VERY_BIG = "4em"


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "font_size": Size.DEFAULT.value,
    "background_color": Color.BACKGROUND.value + "!important",
    "color": Color.DEFAULT_TEXT.value,
    rx.vstack: {"align_items": "center", "justify_content": "center"},
    rx.flex: {
        "align_items": "center",
        "justify_content": "center",
        "flex-direction": "column",
    },
    rx.input: {"background": ""},
    rx.select: {"background": ""},
}


BUS_TITLE_SECTION = {
    "color": Color.TITLES.value,
    "font_weight": FontWeight.BOLD.value,
    "font_size": "1.25em",
}


WEDDING_DATE_HEADER = {
    "font_family": Font.TITLE.value,
    "width": "100%",
    "font_weight": FontWeight.MEDIUM.value,
    "font_style": "normal",
    "text_align": "center",
    "color": Color.TITLES.value,
    "size": "7",
}
