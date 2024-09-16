from typing import List, Optional

import reflex as rx

from wedding.styles import style


def wedding_date_header(
    list_date: List[str], size: Optional[str] = None
) -> rx.Component:
    """
    Creates a heading component for the wedding date.

    Args:
        list_date (List[str]): List of strings representing the wedding date.

    Returns:
        rx.Component: The wedding date header component.
    """

    return rx.heading(" ".join(list_date), size=size, style=style.WEDDING_DATE_HEADER)


def wedding_hour_header(hour: str, size: str) -> rx.Component:
    return rx.heading(hour, size=size, style=style.WEDDING_DATE_HEADER)
