import reflex as rx

from wedding.components import card, icon_section, text_section, title_section
from wedding.utils import IconRoutes, utils

from .confirmation_form import confirmation_form


def confirmation() -> rx.Component:
    return card(
        icon_section(
            icon=IconRoutes.ICON_CONFIRMATION.value, alt=utils.alt_icon_confirmation
        ),
        title_section(title=utils.confirmation_title),
        text_section(text=utils.confirmation_text),
        confirmation_form(),
        id="confirmation_section",
    )
