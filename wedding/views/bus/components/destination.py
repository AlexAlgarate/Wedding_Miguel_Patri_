import reflex as rx

from wedding.components import icon_section
from wedding.styles import FontWeight, Size, style
from wedding.utils import IconRoutes, utils


def destination() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            icon_section(
                icon=IconRoutes.ICON_UBICATION.value,
                width=Size.BIG.value,
                alt=utils.alt_icon_ubication,
            )
        ),
        rx.text(utils.bus_destination_title, style=style.BUS_TITLE_SECTION),
        rx.spacer(),
        _bus_text_destination(),
        width="100",
        align="center",
    )


def _bus_text_destination() -> rx.Component:
    return rx.flex(
        rx.box("Salida de La Agripina "),
        rx.box(
            "a las ",
            rx.text("03:30 ", font_weight=FontWeight.BOLD.value, as_="span"),
            "con destino",
        ),
        rx.text(
            utils.hotel_name,
            font_weight=FontWeight.BOLD.value,
            text_wrap="balance",
            as_="span",
        ),
        rx.text(
            utils.hotel_address,
            font_weight=FontWeight.BOLD.value,
            text_wrap="balance",
            as_="span",
        ),
        rx.box(
            "* El horario de vuelta puede variar.",
            font_size="0.70em",
        ),
        font_size=Size.MAIN_TEXTS.value,
    )
