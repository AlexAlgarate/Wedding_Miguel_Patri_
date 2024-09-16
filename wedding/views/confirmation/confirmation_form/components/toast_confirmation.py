import reflex as rx

from wedding.utils import utils


def toast_confirmation(success: bool, confirm: bool) -> rx.Component:
    return rx.toast(
        utils.toast_accepts_invitation if confirm else utils.toast_decline_invitation,
        position="top-right",
        duration=1800,
        style=(
            {
                "background-color": "#99d674",
                "color": "white",
                "border": "1px solid green",
                "border-radius": "0.53m",
            }
            if success
            else {
                "background-color": "#ff6b6b",
                "color": "white",
                "border": "1px solid red",
                "border-radius": "0.53m",
            }
        ),
    )


# def toast_confirmation() -> rx.Component:
#     return rx.toast.success(
#         "¡Confirmado!",
#         position="top-right",
#         duration=1800,
#         style={
#             "background-color": "#99d674",
#             "color": "white",
#             "border": "1px solid green",
#             "border-radius": "0.53m",
#         },
#     )
