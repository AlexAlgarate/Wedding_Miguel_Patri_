import reflex as rx

# from wedding.api import SupabaseAPI
from wedding.utils import utils
from wedding.views.confirmation.confirmation_form.api import SupabaseAPI
from wedding.views.confirmation.confirmation_form.components import toast_confirmation
from wedding.views.confirmation.confirmation_form.model import SupabaseCredentials

supabase = SupabaseAPI(
    table=utils.supabase_table_name,
    credentials=SupabaseCredentials(),
    supabase_column_names=utils.supabase_name_columns,
)


class FormState(rx.State):
    form_data: dict = {}
    wedding_confirmation: str = ""
    guest_confirmation: str = ""
    other_food_allergies: str = ""

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        supabase.insert_data(form_data)
        yield

    def set_wedding_confirmation(self, value: str):
        self.wedding_confirmation = value

    def set_guest_confirmation(self, value: str):
        self.guest_confirmation = value

    def set_other_food_allergies(self, value: str):
        self.other_food_allergies = value

    # def show_confirmation_toast(self):
    #     if self.wedding_confirmation == utils.OPTIONS_CONFIRMATION_DICT["Yes"]:
    #         return rx.toast(
    #             "¡Confirmado! Gracias por aceptar la invitación.",
    #             position="top-right",
    #             duration=1800,
    #             style={
    #                 "background-color": "#99d674",
    #                 "color": "white",
    #                 "border": "1px solid green",
    #                 "border-radius": "0.53em",
    #             },
    #         )
    #     else:
    #         return rx.toast(
    #             "Invitación declinada. Gracias por informarnos.",
    #             position="top-right",
    #             duration=1800,
    #             style={
    #                 "background-color": "#ff6b6b",
    #                 "color": "white",
    #                 "border": "1px solid red",
    #                 "border-radius": "0.53em",
    #             },
    #         )
    async def show_confirmation_toast(self):
        if self.wedding_confirmation == utils.OPTIONS_CONFIRMATION_DICT["Yes"]:
            return toast_confirmation(True, True)
        else:
            return toast_confirmation(False, False)


"""
class WeddingState(rx.State):
    is_confirmed: bool = False

    def set_confirmation(self, value: bool):
        self.is_confirmed = value

    def show_confirmation_toast(self):
        if self.is_confirmed:
            return rx.toast.success(
                "¡Confirmado!",
                position="top-right",
                duration=1800,
                style={
                    "background-color": "#99d674",
                    "color": "white",
                    "border": "1px solid green",
                    "border-radius": "0.53em",
                },
            )
        else:
            return rx.toast.error(
                "Invitación declinada",
                position="top-right",
                duration=1800,
                style={
                    "background-color": "#ff6b6b",
                    "color": "white",
                    "border": "1px solid red",
                    "border-radius": "0.53em",
                },
            )
rx.button(
    "Enviar",
    type_="submit",
    on_click=WeddingState.show_confirmation_toast,
)
rx.switch(on_change=WeddingState.set_confirmation)

"""
