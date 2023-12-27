import reflex as rx
import datetime as dt

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico",
        ),
        rx.link(
            f"© 2021-{dt.datetime.today().year} VikusS3dev V1 By Felix Orellana",
            href="https://www.linkedin.com/in/felix-saul-orellana-contreras-971b042a6/",
            is_external=True,
        ),
        rx.text(
            "Building with Reflex and Python",
        )
    )
    