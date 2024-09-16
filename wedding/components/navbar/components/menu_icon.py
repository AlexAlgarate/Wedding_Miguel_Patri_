import reflex as rx


def menu_icon(tag: str, color: str = "transparent") -> rx.Component:
    """
    Creates a menu icon component with the specified tag and color.

    Args:
        tag (str): The tag for the icon.
        color (str): The color of the icon. Defaults to "transparent".

    Returns:
        rx.Component: The menu icon component.
    """

    return rx.icon(
        tag=tag,
        color=color,
        margin="12px 16px",
        size=24,
        custom_attrs={
            "aria-haspopup": "true",
            "aria-expanded": "false",
            "aria-controls": "menu-content",
            "role": "button",
        },
    )
