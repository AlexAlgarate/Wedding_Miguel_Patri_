import reflex as rx

from wedding.styles import Color, Font, FontWeight
from wedding.utils import utils


def farewell_message() -> rx.Component:
    """
    Creates a centered heading component for a farewell
    message displayed at the bottom of the page.

    Returns:
        rx.Component: The farewell message component.
    """

    return rx.center(
        rx.heading(
            utils.bottom_text,
            size="8",
            font_family=Font.TITLE.value,
            font_weight=FontWeight.MEDIUM.value,
            font_style="normal",
            line_height="normal",
            color=Color.TITLES.value,
            position="relative",
            top="50px",
        )
    )
