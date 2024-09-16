import reflex as rx

from wedding.styles import Color, Font, FontHeight, FontWeight


def title_section(title: str) -> rx.Component:
    """
    Creates a title section with the specified title.

    Args:
        title (str): The title text.

    Returns:
        rx.Component: The title section component.
    """

    return rx.heading(
        title,
        font_size=[
            "30px",
            "30px" "30px",
            "36px",
            "36px",
        ],
        font_weight=FontWeight.MEDIUM.value,
        text_align="center",
        width="100%",
        letter_spacing="0.0125rem",
        line_height=FontHeight.MEDIUM.value,
        font_family=Font.TITLE.value,
        color=Color.TITLES.value,
    )
