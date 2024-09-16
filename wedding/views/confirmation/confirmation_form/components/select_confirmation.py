from typing import Dict, Optional

import reflex as rx


def select_confirmation(
    options: Dict[str, str],
    placeholder: str,
    name: str,
    label: str = None,
    on_change_event: Optional[rx.EventHandler] = None,
) -> rx.Component:
    """
    Creates a reusable select input field component for the form.

    Args:
        options (list): List of options for the select field.
        placeholder (str): Placeholder text.
        name (str): Name of the input field.
        label (str): Label of the input field.
        on_change_event (Optional): Event handler for onChange event.

    Returns:
        rx.Component: The select input field.
    """
    return rx.vstack(
        rx.select(
            options,
            placeholder=placeholder,
            label=label,
            name=name,
            required=True,
            on_change=on_change_event,
        ),
    )
