import reflex as rx
import datetime as dt
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
import link_bio.my_info as my_info
import link_bio.constants as constants


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
        ),
        rx.link(
            f"© 2021-{dt.datetime.today().year} VikusS3dev V1 By {my_info.NOMBRE_Y_APELLIDO}",
            href= constants.LINKEDIN_URL,
            is_external=True,
            font_size=Size.MEDIUM.value,
           
        ),
        rx.text(
            "Building with Reflex and Python",
            font_size=Size.MEDIUM.value,
            maring_top=Size.ZERO.value,
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER_COLOR.value,
    )
    