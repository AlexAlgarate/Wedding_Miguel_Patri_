import reflex as rx

from wedding.utils import FileRoutes, utils


def lavender_flowers(
    alt: str,
    image: str,
    margin_type: bool = True,
) -> rx.Component:
    """
    Create a mobile-only component displaying an image with optional margin adjustments.

    Parameters:
    - image (str): The path or URL of the image.
    - margin_type (bool): If True, applies a specific margin for the image.

    Returns:
    - rx.Component: A Reflex component representing the mobile-only image.
    """

    return rx.mobile_only(
        rx.cond(
            margin_type,
            rx.image(
                src=image,
                width="100%",
                height="100%",
                flex_shrink="0",
                position="relative",
                margin_bottom="-120px",
                z_index="1",
                alt=alt,
            ),
            rx.image(
                src=image,
                width="100%",
                height="100%",
                flex_shrink="0",
                margin_top="-139px",
                z_index="1",
                alt=alt,
            ),
        )
    )


def flowers_between_section() -> rx.Component:
    """
    Create a mobile-only component displaying an image with optional margin adjustments.

    Parameters:
    - image (str): The path or URL of the image.
    - margin_type (bool): If True, applies a specific margin for the image.

    Returns:
    - rx.Component: A Reflex component representing the mobile-only image.
    """

    return rx.mobile_only(
        rx.image(
            src=FileRoutes.IMAGE_LEAFS_SECTION.value,
            width="100%",
            height="100%",
            flex_shrink="0",
            alt=utils.alt_image_leafs,
        )
    )
