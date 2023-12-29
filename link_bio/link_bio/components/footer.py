import reflex as rx
import datetime as dt
from link_bio.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico",
        ),
        rx.link(
            f"© 2021-{dt.datetime.today().year} VikusS3dev V1 By Saul Orellana",
            href="https://www.linkedin.com/in/felix-saul-orellana-contreras-971b042a6/",
            is_external=True,
            font_size=Size.MEDIUM.value,
            maring_top="0px !important",
        ),
        rx.text(
            "Building with Reflex and Python",
            font_size=Size.MEDIUM.value,
        ),
        margin_bottom=Size.BIG.value,
    )
    