from enum import Enum


def icon_route(filename: str, png: bool = False, webp: bool = False) -> str:
    """
    Generate a route for an icon file based on the provided filename and format options.

    Args:
        filename (str): The name of the icon file.
        png (bool): Whether to generate a route for a PNG format. Defaults to False.
        webp (bool): Whether to generate a route for a WEBP format. Defaults to False.

    Returns:
        str: The route for the icon file.
    """

    format_extensions = {"png": ".png", "webp": ".webp", "default": ".svg"}
    selected_format = "default" if not (png or webp) else "png" if png else "webp"

    return f"/icons/{filename}{format_extensions[selected_format]}"


def image_route(filename: str, svg: bool = False) -> str:
    """
    Generate a route for an image file based on the provided filename and format options.

    Args:
        filename (str): The name of the image file.
        svg (bool, optional): Whether to generate a route
        for an SVG format. Defaults to False.

    Returns:
        str: The route for the image file.
    """

    format_extension = ".svg" if svg else ".webp"

    return f"/images/{filename}{format_extension}"


class Route(Enum):
    INDEX = "/"
    CONTACT = "/contact"


class FileRoutes(Enum):
    JS_COUNTDOWN = "/js/countdown.js"
    IMAGE_HEADER = image_route("miguel_patri")
    IMAGE_AGRIPINA = image_route("valdeluz")
    IMAGE_LAVENDER_TOP = image_route("lavender_top")
    IMAGE_LAVENDER_BOTTOM = image_route("lavender_bottom")
    IMAGE_LEAFS_SECTION = image_route("leafs", svg=True)


class IconRoutes(Enum):
    ICON_BUS = icon_route("bus")
    ICON_CAMERA = icon_route("camera")
    ICON_CELEBRATION = icon_route("wedding")
    ICON_CONFIRMATION = icon_route("confirmation")
    ICON_UBICATION = icon_route("localization", webp=True)
    ICON_GIFT = icon_route("present", webp=True)
    ICON_WHATSAPP = icon_route("whatsapp")
    ICON_EMAIL = icon_route("email")
    ICON_PHONE = icon_route("phone")
