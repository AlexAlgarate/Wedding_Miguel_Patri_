import reflex as rx

config = rx.Config(
    app_name="wedding",
    cors_allowed_origins=[
        "http://localhost:3000/",
        "https://wedding-patri-miguel.vercel.app/",
    ],
)
