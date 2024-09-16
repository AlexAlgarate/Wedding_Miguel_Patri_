import reflex as rx

from wedding.components import icon_section
from wedding.styles import FontWeight, Size, style
from wedding.utils import IconRoutes, utils


def origin() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            icon_section(
                icon=IconRoutes.ICON_UBICATION.value,
                width=Size.BIG.value,
                alt=utils.alt_icon_ubication,
            ),
        ),
        rx.text(utils.bus_origin_title, style=style.BUS_TITLE_SECTION),
        rx.spacer(),
        _bus_text_origin(),
        width="100%",
        align="center",
    )


def _bus_text_origin() -> rx.Component:
    return rx.flex(
        rx.box(
            "Salida ",
            rx.text(
                utils.origin_bus_schedule, font_weight=FontWeight.BOLD.value, as_="span"
            ),
            " desde ",
        ),
        rx.box(
            rx.text(
                utils.hotel_name,
                font_weight=FontWeight.BOLD.value,
                as_="span",
            ),
        ),
        rx.box(
            rx.text(
                utils.hotel_address,
                font_weight=FontWeight.BOLD.value,
                as_="span",
            ),
        ),
        font_size=Size.MAIN_TEXTS.value,
    )
