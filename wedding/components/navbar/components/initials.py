import reflex as rx

from wedding.styles import Color, Font, FontWeight, Size


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


def initials_navbar() -> rx.Component:
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
        _hover={"text_decoration": "none"},
    )
