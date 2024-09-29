import reflex as rx

from wedding.components import (
    farewell_message,
    flowers_between_section,
    lavender_flowers,
)
from wedding.styles import style as style
from wedding.utils import FileRoutes, utils
from wedding.views import (
    accomodation,
    bus_service,
    celebration,
    confirmation,
    countdown,
    google_photo,
    header,
    navbar,
    wedding_gifts,
)


@rx.page(
    title=utils.title_main,
    description=utils.description_main,
    image=FileRoutes.IMAGE_HEADER.value,
)
def index() -> rx.Component:
    return rx.vstack(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        lavender_flowers(
            alt=utils.alt_image_lavender,
            image=FileRoutes.IMAGE_LAVENDER_TOP.value,
        ),
        rx.vstack(
            rx.flex(
                header(),
                countdown(),
                flowers_between_section(),
                confirmation(),
                celebration(),
                wedding_gifts(),
                flowers_between_section(),
                accomodation(),
                bus_service(),
                flowers_between_section(),
                google_photo(),
                gap="16px",
                width="100%",
                max_width=style.MAX_WIDTH,
            ),
            width="auto",
        ),
        farewell_message(),
        lavender_flowers(
            alt=utils.alt_image_lavender,
            image=FileRoutes.IMAGE_LAVENDER_BOTTOM.value,
            margin_type=False,
        ),
        width="100%",
    )
