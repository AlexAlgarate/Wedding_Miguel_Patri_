from typing import Dict, List

import reflex as rx


def create_personal_info_form(personal_info: List[Dict[str, str]]) -> rx.Component:
    personal_inputs = [
        rx.input(
            placeholder=item["placeholder"],
            name=item["name"],
            type=item["type"],
            required=True,
            width="auto",
        )
        for item in personal_info
    ]
    return rx.vstack(
        *personal_inputs,
        spacing="4",
        width="100%",
    )
