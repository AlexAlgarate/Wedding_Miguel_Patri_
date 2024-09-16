from typing import Dict

import reflex as rx

from wedding.styles import Color

from .link_navbar import link_navbar
from .menu_icon import menu_icon


def menu_burger(data: Dict[str, str]) -> rx.Component:
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
            link_navbar(title=title, url=url),
            color_scheme="purple",
        )
        for title, url in data.items()
    ]

    return rx.menu.root(
        rx.menu.trigger(
            menu_icon(tag="menu", color=Color.TITLES.value),
            _hover={"cursor": "pointer"},
        ),
        rx.menu.content(
            *menu_items,
            size="2",
        ),
    )
