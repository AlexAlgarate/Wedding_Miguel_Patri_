from typing import Dict, Optional

import reflex as rx

from wedding.styles import Color, Font, FontWeight, Size
from wedding.utils import utils


def _link_navbar(title: str, url: str) -> rx.Component:
    """
    Creates a navigation link component for the navbar.

    Args:
        title (str): The text to display on the link.
        url (str): The URL the link points to.

    Returns:
        rx.Component: The navigation link component.
    """

    return rx.link(
        rx.text(
            title,
            font_weight=FontWeight.LIGHT.value,
            font_size=Size.DEFAULT.value,
        ),
        href=url,
        is_external=False,
        text_align="start",
    )


def _menu_icon(tag: str, color: Optional[str] = None) -> rx.Component:
    """
    Creates a menu icon component with the specified tag and color.

    Args:
        tag (str): The tag for the icon.
        color (str): The color of the icon. Defaults to "transparent".

    Returns:
        rx.Component: The menu icon component.
    """

    return rx.icon(
        tag=tag,
        color="transparent" if not color else color,
        margin="12px 16px",
        size=24,
        custom_attrs={
            "aria-haspopup": "true",
            "aria-expanded": "false",
            "aria-controls": "menu-content",
            "role": "button",
        },
    )


def _capital_letter_initial(letter: str) -> rx.Component:
    """
    Creates a span with the specified capital letter and font size.

    Args:
        letter (str): The capital letter.

    Returns:
        rx.Component: The capital letter component.
    """

    return rx.text(
        letter.upper(),
        font_size=[
            Size.BIG_TITLES.value,
            Size.MEDIUM_BIGGER.value,
            Size.MEDIUM_BIGGER.value,
            Size.MEDIUM_BIGGER.value,
            Size.MEDIUM_BIGGER.value,
        ],
        as_="span",
    )


def _menu_burger(data: Dict[str, str]) -> rx.Component:
    """
    Creates a menu burger component.

    Args:
        data (Dict[str, str]): A dictionary containing
        menu items with their titles and URLs.

    Returns:
        rx.Component: The menu burger component.
    """

    menu_items = [
        rx.menu.item(
            _link_navbar(title=title, url=url),
            color_scheme="purple",
        )
        for title, url in data.items()
    ]

    return rx.menu.root(
        rx.menu.trigger(
            _menu_icon(tag="menu", color=Color.TITLES.value),
            _hover={"cursor": "pointer"},
        ),
        rx.menu.content(
            *menu_items,
            size="2",
        ),
    )


def _initials_navbar() -> rx.Component:
    """
    Creates the initials component for the navbar.

    Returns:
        rx.Component: The initials navbar component.
    """

    return rx.link(
        rx.box(
            _capital_letter_initial("M"),
            rx.text("&", font_size="1.75em", as_="span"),
            _capital_letter_initial("P"),
            height="100%",
            font_weight=FontWeight.MEDIUM.value,
            color=Color.TITLES.value,
            font_family=Font.TITLE.value,
            letter_spacing="5px",
        ),
        href="/",
        is_external=False,
    )


def navbar() -> rx.Component:
    """
    Creates a responsive navbar component with a menu bar, initials, and a notification bell.

    Returns:
        rx.Component: The navbar component.
    """

    return rx.hstack(
        _menu_burger(
            data=utils.menu_data,
        ),
        rx.spacer(),
        _initials_navbar(),
        rx.spacer(),
        _menu_icon(tag="bell"),
        class_name="navbar_wedding",
        id="navbar",
        box_shadow=f"0px 1px 5px 1px {Color.PURPLE_OPACITY.value}",
        position="sticky",
        padding_top=Size.MEDIUM_SMALL.value,
        padding_bottom=Size.ZERO.value,
        z_index="5",
        justify_content="center",
        top="0",
        background_color=Color.CONTENT.value,
        width="100%",
        align="center",
        justify="center",
    )
