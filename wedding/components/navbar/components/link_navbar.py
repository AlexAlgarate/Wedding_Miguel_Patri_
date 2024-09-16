import reflex as rx

from wedding.styles import FontWeight, Size


def link_navbar(title: str, url: str) -> rx.Component:
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
        text_decoration="none",
        _hover={"text_decoration": "none"},
    )
