from typing import Optional

import reflex as rx

from wedding.styles import FontWeight, Size, style


def text_section(
    text: str, font_weight: Optional[str] = FontWeight.LIGHT.value
) -> rx.Component:
    """
    Creates a text section with the specified text and optional font weight.

    Args:
        text (str): The text content.
        font_weight (Optional[str]): The font weight. Defaults to FontWeight.LIGHT.value.

    Returns:
        rx.Component: The text section component.
    """

    return rx.text(
        text,
        font_weight=font_weight,
        max_width=style.MAX_WIDTH,
        padding=Size.SMALL.value,
        text_align="center",
        font_size=[
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
        ],
        text_wrap="pretty",
        font_style="normal",
        line_height="normal",
        width="100%",
    )
