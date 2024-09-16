import reflex as rx

from wedding import utils as utils
from wedding.state import FormState
from wedding.views.confirmation.confirmation_form.components import (
    select_confirmation,
    text_area,
)


def select_confirm_companion() -> rx.Component:
    return rx.vstack(
        select_confirmation(
            options=["Sí, voy con acompañantes", "No, solo yo"],
            placeholder="¿Vienes con acompañantes?",
            name="wedding_companion",
            required=True,
            label="Vienes con acompañantes?",
            on_change_event=FormState.set_guest_confirmation,
        ),
        rx.cond(
            FormState.guest_confirmation == "Sí, voy con acompañantes",
            rx.vstack(
                rx.select(
                    utils.number_adults,
                    label="Nº de adultos",
                    placeholder="Nº de adultos en total",
                    name="number_adults",
                    required=True,
                ),
                rx.select(
                    utils.number_kids,
                    label="Nº de niños",
                    placeholder="Nº de niños",
                    name="number_kids",
                    required=True,
                ),
                text_area(
                    placeholder="Escribe el nombre de los acompañantes",
                    name="name_companion",
                    required=True,
                ),
                text_area(
                    placeholder="Alergias o intolerancias de los asistentes",
                    name="food_allergies",
                    required=True,
                ),
                width="100%",
            ),
            rx.cond(
                FormState.guest_confirmation == "No, solo yo",
                text_area(
                    placeholder="¿Tienes alguna alergia o intolerancia?",
                    name="food_allergies",
                    required=True,
                ),
            ),
        ),
        width="100%",
    )
