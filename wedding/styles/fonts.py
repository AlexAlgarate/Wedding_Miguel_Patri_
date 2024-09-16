from enum import Enum


class Font(Enum):
    TITLE = "Elsie"
    DEFAULT = "Raleway"


class FontWeight(Enum):
    LIGHT = "300"
    MEDIUM_INSIDE_TEXTS = "450"
    MEDIUM = "500"
    HIGH = "600"
    BOLD = "800"


class FontHeight(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    NORMAL = "normal"
    MEDIUM = "1.25em"
    BIG = "2em"
