from typing import Dict

import reflex as rx

from wedding.components import secondary_button
from wedding.utils import IconRoutes, utils


def whatsapp_button(*contacts: Dict[str, str]) -> rx.Component:
    """
    Creates a reflex component to display WhatsApp buttons for multiple contacts.

    Args:
        contacts (Dict[str, str]): Dictionary containing contact information.

    Returns:
        rx.Component: Reflex component displaying WhatsApp buttons.
    """

    whatsapp_buttons = [
        secondary_button(
            f"Abrir Whatsapp con {contact.get('name')}",
            f"https://wa.me/34{contact.get('phone_number').replace(' ', '')}",
            IconRoutes.ICON_WHATSAPP.value,
            utils.alt_icon_whatsapp,
        )
        for contact in contacts
    ]
    return rx.flex(*whatsapp_buttons, gap="8px")
