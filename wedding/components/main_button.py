import reflex as rx

from wedding.styles import Color, Size
from wedding.styles.fonts import FontWeight


def main_button(button_name: str, url: str, z_index: str = "0") -> rx.Component:
    """
    Creates a main button component with a link.

    Args:
        button_name (str): The text to display on the button.
        url (str): The URL the button links to.
        **args: Additional arguments for the button.

    Returns:
        rx.Component: The main button component.
    """
    style_main_button = dict(
        width="100%",
        font_size=[
            Size.DEFAULT.value,
            Size.DEFAULT.value,
            Size.DEFAULT.value,
            Size.DEFAULT.value,
            Size.LARGE.value,
        ],
        padding=[
            "16px 24px",
            "16px 24px",
            "16px 24px",
            "16px 24px",
            "20px 24px",
        ],
        color=Color.BACKGROUND.value,
        background=Color.BUTTONS.value,
        border_radius="5px",
        border="2px solid #4F1F7E",
        text_align="center",
        margin_bottom=Size.DEFAULT.value,
        _hover={
            "background": "rgba(80, 69, 135, 0.91)",
            "cursor": "pointer",
        },
        font_weight=FontWeight.HIGH.value,
    )
    return rx.link(
        rx.button(button_name, style=style_main_button),
        href=url,
        is_external=True,
        z_index=z_index,
    )
