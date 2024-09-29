import reflex as rx

from wedding.components import (
    icon_section,
    secondary_button,
    text_section,
    title_section,
)
from wedding.utils import FileRoutes, IconRoutes, urls, utils

from .components import image_celebration, text_celebration


def celebration() -> rx.Component:
    return rx.flex(
        icon_section(
            icon=IconRoutes.ICON_CELEBRATION.value, alt=utils.alt_icon_celebration
        ),
        title_section(title=utils.celebration_title),
        text_section(utils.celebration_text),
        image_celebration(image=FileRoutes.IMAGE_AGRIPINA.value),
        text_celebration(),
        secondary_button(
            button_name=utils.celebration_button,
            url=urls.MONTEALVAR_MAPS_URL,
        ),
        align_self="stretch",
        gap="8px",
        scroll_margin_top="75px",
        id="celebration_section",
    )
