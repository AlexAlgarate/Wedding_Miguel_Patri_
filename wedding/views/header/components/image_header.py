import reflex as rx

from wedding.utils import FileRoutes, utils


def image_header() -> rx.Component:
    """
    Creates an image component for the header.

    Returns:
        rx.Component: The header image component.
    """

    return rx.image(
        src=FileRoutes.IMAGE_HEADER.value,
        alt=utils.alt_image_partners,
        width="100%",
        height="50%",
        box_shadow="0px 8px 5px 1px #F8F8FA inset",
        align_self="stretch",
        padding="-6px 12px",
    )
