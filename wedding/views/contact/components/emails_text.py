from typing import Dict

import reflex as rx

from wedding.styles import Size


def emails_text_component(*contact: Dict[str, str]) -> rx.Component:
    """
    Creates a reflex component to display email text.

    Args:
        contact (Dict[str, str]): Dictionary containing email information.

    Returns:
        rx.Component: Reflex component displaying email text.
    """

    emails_list = [create_single_email(email=email) for email in contact]
    return rx.flex(*emails_list, gap="8px")


def create_single_email(email: Dict[str, str]) -> rx.Component:
    """
    Creates a reflex component for a single email.

    Args:
        email (Dict[str, str]): Dictionary containing email information.

    Returns:
        rx.Component: Reflex component for a single email.
    """

    return rx.text(
        email["email"],
        font_size=[
            "1.2em",
            "1.2em",
            "1.2em",
            "1.2em",
            Size.LARGE.value,
        ],
        font_weight="600",
    )
