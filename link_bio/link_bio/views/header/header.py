import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="vikusS3 dev", size="xl"),
            rx.vstack(
                rx.heading(
                    "Hola ✌ MI NOMBRE ES VIKUS",
                    size="lg"),
                rx.text(
                    "@vikusss3dev",
                    maring_top="0px !important",
                ),
                rx.hstack(
                    link_icon("https://github.com/VikusS3"),
                    link_icon("https://github.com/VikusS3"),
                    link_icon("https://github.com/VikusS3"),    
                ),
                align_items="start",
            ),
            spacing=Size.BIG.value,
        ),
        
        rx.flex(
            info_text("Edad:", "21 años"),
            rx.spacer(),
            info_text("Ciudad:", "Lima, Perú"),
            rx.spacer(),
            info_text("Email:", "felix21soc@gmail.com"),
            width="100%",
        ),
        
        
        rx.text("""Soy tecnico en sistemas y programador con mas de un año de experiencia.
                Actualmente trabajo como freelance full-stack developer python, php y ASP.NET.
                Ademos de ser un apasionado por la tecnologia, me gusta mucho la musica y los 
                videojuegos."""),
        spacing=Size.BIG.value,
        align_items="start",
    )