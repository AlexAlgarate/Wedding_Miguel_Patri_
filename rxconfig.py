import reflex as rx

config = rx.Config(
    app_name="wedding",
    backend_port=8080,
    cors_allowed_origins=[
        # "http://localhost:3000/",
        # "http://localhost:8000/",
        # "https://wedding-patri-miguel.vercel.app/",
    ],
)
