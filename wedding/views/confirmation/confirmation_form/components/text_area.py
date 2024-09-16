import reflex as rx


def text_area(name: str, placeholder: str, required: bool = True) -> rx.Component:
    """
    Creates a reusable text area input field component.

    Args:
        name (str): Name of the input field.
        placeholder (str): Placeholder text.
        required (bool): Whether the input field is required (default is True).

    Returns:
        rx.Component: The text area input field.
    """
    return rx.text_area(
        placeholder=placeholder,
        name=name,
        size="3",
        resize="both",
        radius="medium",
        required=required,
    )
