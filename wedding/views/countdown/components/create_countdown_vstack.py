import reflex as rx

from wedding.styles import Color, Font, FontHeight, FontWeight, Size


def create_countdown_vstack(element: str, text_date: str) -> rx.Component:
    """
    Creates a vstack component for countdown numbers and corresponding text date.

    Args:
        element (str): The countdown element.
        text_date (str): The text date.

    Returns:
        rx.Component: The vstack component.
    """

    return rx.vstack(
        _countdown_numbers(element=element),
        _element_date(text_date=text_date),
    )


def _countdown_numbers(element: str) -> rx.Component:
    """
    Creates a text component for displaying countdown numbers.

    Args:
        element (str): The countdown element.

    Returns:
        rx.Component: The countdown numbers component.
    """

    return rx.text(
        id=element,
        color=Color.NUMBERS_COUNTDOWN.value,
        width="100%",
        height="100%",
        font_family=Font.TITLE.value,
        text_align="center",
        font_style="normal",
        font_weight=FontWeight.MEDIUM_INSIDE_TEXTS.value,
        line_height=FontHeight.NORMAL.value,
        font_size=[
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
            Size.BIG.value,
        ],
    )


def _element_date(text_date: str) -> rx.Component:
    """
    Creates a text component for displaying countdown text date.

    Args:
        text_date (str): The text date.

    Returns:
        rx.Component: The element date component.
    """

    return rx.text(
        text_date,
        color=Color.TEXT_COUNTDOWN.value,
        text_align="center",
        font_family=Font.DEFAULT.value,
        font_size="16px",
        font_style="normal",
        font_weight=FontWeight.MEDIUM_INSIDE_TEXTS.value,
        line_height=FontHeight.NORMAL.value,
    )
