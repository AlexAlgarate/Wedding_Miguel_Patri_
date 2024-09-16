from typing import Optional

import reflex as rx

from wedding.styles import Color, Size


def secondary_button(
    button_name: str,
    url: str,
    icon: Optional[str] = None,
    alt: Optional[str] = None,
) -> rx.Component:
    """
    Create a reflex component for a secondary button.

    Args:
        button_name (str): Name of the button.
        url (str): URL to link the button to.
        icon (Optional[str]): Optional icon source.
        alt (Optional[str]): Optional description of the icon image.

    Returns:
        rx.Component: Reflex component for a secondary button.
    """
    style_secondary_button = dict(
        color=Color.TITLES.value,
        text_align="center",
        font_variant_numeric="lining-nums proportional-nums",
        padding=[
            "8px 24px",
            "8px 24px",
            "8px 24px",
            "8px 24px",
            "16px 24px",
        ],
        justify_content="center",
        align_items="center",
        gap="8px",
        align_self="stretch",
        border_radius="5px",
        border="2px solid #4F1F7E",
        background=Color.BACKGROUND.value,
        font_size=[
            Size.DEFAULT.value,
            Size.DEFAULT.value,
            Size.DEFAULT.value,
            Size.DEFAULT.value,
            Size.LARGE.value,
        ],
        _hover={"cursor": "pointer", "background": "#f4f2fa"},
    )
    button_content = []

    if icon:
        button_content.append(
            rx.image(
                src=icon,
                alt=alt,
            )
        )

    button_content.append(rx.text(button_name))

    return rx.link(
        rx.button(*button_content, style=style_secondary_button),
        href=url,
        is_external=True,
    )
