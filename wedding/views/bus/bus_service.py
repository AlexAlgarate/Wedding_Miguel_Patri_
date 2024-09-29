import reflex as rx

from wedding.components import card, icon_section, text_section, title_section
from wedding.utils import IconRoutes, utils

from .components import destination


def bus_service() -> rx.Component:
    return card(
        icon_section(icon=IconRoutes.ICON_BUS.value, alt=utils.alt_icon_bus),
        title_section(title=utils.bus_title),
        text_section(utils.bus_text),
        destination(),
        id="bus_service_section",
    )
