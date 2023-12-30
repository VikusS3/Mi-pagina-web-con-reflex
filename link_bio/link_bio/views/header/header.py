import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
import link_bio.constants as constants
import link_bio.my_info as my_info
from link_bio.styles.colors import TextColor as TextColor
from link_bio.components.title import title
from link_bio.styles.colors import Color as Color


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="VikusS3 dev",
                src="avatar.jpg", 
                size="xl",
                color=Color.BACKGROUND_COLOR.value,
                bg=Color.PRIMARY_COLOR.value,
                padding="2px",
                boder="5px",
                boder_color=Color.PRIMARY_COLOR.value,
            ),
            rx.vstack(
                rx.heading(
                    "saul orellana",
                    size="lg",
                    color=TextColor.HEADER_COLOR.value,
                ),
                rx.text(
                    "@vikusss3dev",
                    maring_top=Size.ZERO.value,
                    color = TextColor.BODY_COLOR.value,
                ),
                rx.hstack(
                    link_icon(
                        "icons/github.svg",
                        constants.GITHUB_URL,
                    ),
                    link_icon(
                        "icons/github-alt.svg",
                        constants.SECONDARY_ACCOUNT_GITHUB_URL,
                    ),
                    link_icon(
                        "icons/facebook.svg",
                        constants.FACEBOOK_URL,
                    ),
                    spacing=Size.BIG.value,
                ),
                align_items="start",
            ),
            spacing=Size.BIG.value,
        ),
        
        rx.flex(
            info_text("Edad:", f"{my_info.EDAD} años"),
            rx.spacer(),
            info_text("Ciudad:", my_info.CIUDAD),
            rx.spacer(),
            info_text("Email:", my_info.EMAIL),
            width="100%",
        ),
        
        
        rx.text(
                """Soy tecnico en sistemas y programador con mas de un año de experiencia.
                Actualmente trabajo como freelance full-stack developer python, php y ASP.NET.
                Ademos de ser un apasionado por la tecnologia, me gusta mucho la musica y los 
                videojuegos.""",
                font_size=Size.DEFAULT.value,
                color=TextColor.BODY_COLOR.value,),
        spacing=Size.BIG.value,
        align_items="start",
    )