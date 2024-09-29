import reflex as rx

from wedding.components import icon_section
from wedding.styles import Size, style
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
        _bus_text_destination(),
        width="100",
        align="center",
    )


def _bus_text_destination() -> rx.Component:
    return rx.flex(
        rx.text(
            "Salida de Montealvar a las ",
            rx.text.strong("05:00 "),
            "con destino ",
            rx.text.strong("Guadalajara"),
            ".",
            align="center",
        ),
        rx.box(
            "* El horario de vuelta puede variar.",
            font_size="0.70em",
        ),
        font_size=Size.MAIN_TEXTS.value,
    )
