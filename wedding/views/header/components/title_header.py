import reflex as rx

from wedding.styles import Color, Font, FontWeight


def title_header() -> rx.Component:
    """
    Creates a flex container for the title header.

    Returns:
        rx.Component: The title header component.
    """

    return rx.vstack(
        rx.mobile_and_tablet(
            rx.flex(
                _title("¡Nos"),
                _title("casamos!"),
            ),
            margin_top="-85px",
        ),
        rx.desktop_only(
            rx.flex(
                _title("¡Nos"),
                _title("casamos!"),
                id="header_desktop",
            )
        ),
    )


def _title(text: str) -> rx.Component:
    """
    Creates a heading component with the specified text and style.

    Args:
        text (str): The text for the heading.

    Returns:
        rx.Component: The heading component.
    """

    return rx.heading(
        text,
        font_family=Font.TITLE.value,
        font_weight=FontWeight.MEDIUM.value,
        font_style="normal",
        line_height="normal",
        color=Color.TITLES.value,
        font_size=["36px", "36px", "48px", "48px", "48px"],
    )
