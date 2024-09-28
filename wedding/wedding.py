import reflex as rx

from wedding.pages import index
from wedding.styles import style

app = rx.App(
    stylesheets=style.STYLESHEETS,
    theme=rx.theme(
        appearance="dark",
    ),
    style=style.BASE_STYLE,
)


def hello():
    return "hello"


def hello_user(user: str):
    return {"message": f"hello {user} jodeeeeeeeeer"}


app.api.add_api_route("/hello", hello)
app.api.add_api_route("/hello_user/{user}", hello_user)
app.add_page(index)
