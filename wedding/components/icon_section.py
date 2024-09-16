from typing import Optional

import reflex as rx

from wedding.styles import Color, Size


def icon_section(alt: str, icon: str, width: Optional[str] = None) -> rx.Component:
    """
    Creates an image component representing an icon.

    Args:
        icon (str): The URL or path to the icon image.
        width (Optional[str]): The width of the icon. If None, a default size is used.

    Returns:
        rx.Component: The icon section component.
    """

    return rx.image(
        src=icon,
        color=Color.DEFAULT_TEXT.value,
        width=width if width is not None else Size.VERY_BIG.value,
        max_height="auto",
        alt=alt,
    )
