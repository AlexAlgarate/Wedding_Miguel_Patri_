import reflex as rx

from wedding.pages import index
from wedding.styles import style

app = rx.App(
    stylesheets=style.STYLESHEETS,
    theme=rx.theme(
        appearance="light",
    ),
    style=style.BASE_STYLE,
)


def hello():
    return "hello"


app.api.add_api_route("/hello", hello)
app.add_page(index)
