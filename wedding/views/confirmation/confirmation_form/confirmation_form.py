import reflex as rx

from wedding.styles import style as style
from wedding.utils import utils
from wedding.views.confirmation.confirmation_form.components import (  # toast_confirmation,
    create_personal_info_form,
    select_confirmation,
    text_area,
)
from wedding.views.confirmation.confirmation_form.state.form_state import FormState


def _render_companion_details() -> rx.Component:
    """
    Creates a form section for guests who are attending the wedding with companions.
    This section includes input fields for the number of adults, number of children,
    names of the companions, and any food allergies or intolerances.

    Returns:
        rx.Component: The companion details form.
    """
    return rx.vstack(
        select_confirmation(
            options=utils.number_adults,
            label="Nº de adultos",
            placeholder="Nº de adultos en total",
            name="number_adults",
        ),
        select_confirmation(
            options=utils.number_kids,
            label="Nº de niños",
            placeholder="Nº de niños",
            name="number_kids",
        ),
        text_area(
            placeholder="Escribe el nombre de los acompañantes",
            name="name_companion",
        ),
        text_area(
            placeholder="Alergias o intolerancias de los asistentes",
            name="food_allergies",
        ),
        width="100%",
    )


def _render_no_companion_details() -> rx.Component:
    """
    Creates a form section for guests who are attending the wedding without companions.
    It asks for any food allergies or intolerances only.

    Returns:
        rx.Component: The no companion section.
    """
    return rx.cond(
        FormState.guest_confirmation == utils.OPTIONS_COMPANIONN_DICT["No_companion"],
        text_area(
            placeholder="¿Tienes alguna alergia o intolerancia?",
            name="food_allergies",
        ),
    )


def _render_companion_confirmation_section() -> rx.Component:
    """
    Creates a section where guests confirm whether they're bringing companions,
    and renders appropriate forms based on their response.

    Returns:
        rx.Component: The companion confirmation section.
    """
    return rx.vstack(
        select_confirmation(
            options=list(utils.OPTIONS_COMPANIONN_DICT.values()),
            placeholder="¿Vienes con acompañantes?",
            name="wedding_companion",
            label="Vienes con acompañantes?",
            on_change_event=FormState.set_guest_confirmation,
        ),
        rx.cond(
            FormState.guest_confirmation
            == utils.OPTIONS_COMPANIONN_DICT["Yes_companion"],
            _render_companion_details(),
            _render_no_companion_details(),
        ),
        width="100%",
    )


def _render_confirmed_guest_questions() -> rx.Component:
    """
    Renders a section for confirmed guests, including a form for personal information
    and the companion confirmation section.

    Returns:
        rx.Component: The questions section for guests attending the wedding.
    """
    return rx.cond(
        FormState.wedding_confirmation == utils.OPTIONS_CONFIRMATION_DICT["Yes"],
        rx.vstack(
            create_personal_info_form(personal_info=utils.personal_info_dict),
            _render_companion_confirmation_section(),
            width="100%",
        ),
    )


def _render_wedding_response_form() -> rx.Component:
    """
    Creates the main wedding response form. If the guest is not attending,
    only the personal information form is rendered. If attending,
    the guest details and companion details sections are shown.

    Returns:
        rx.Component: The wedding response form.
    """
    return rx.cond(
        FormState.wedding_confirmation == utils.OPTIONS_CONFIRMATION_DICT["No"],
        rx.vstack(
            create_personal_info_form(personal_info=utils.personal_info_dict),
        ),
        _render_confirmed_guest_questions(),
    )


def confirmation_form() -> rx.Component:
    return rx.vstack(
        rx.toast.provider(),
        rx.form(
            rx.vstack(
                rx.text("SE RUEGA CONFIRMACIÓN"),
                select_confirmation(
                    options=list(utils.OPTIONS_CONFIRMATION_DICT.values()),
                    placeholder="¿Asistirás a nuestra boda?",
                    name="confirm_invitation",
                    on_change_event=FormState.set_wedding_confirmation,
                ),
                _render_wedding_response_form(),
                rx.button(
                    "Enviar",
                    type="submit",
                    _hover={"cursor": "pointer"},
                    on_click=FormState.show_confirmation_toast,
                ),
                width="100%",
                spacing="4",
            ),
            on_submit=FormState.handle_submit,
        ),
        max_width=style.MAX_WIDTH,
        width="100%",
    )
