import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
           rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            ), 
        ),
        footer()
    )

app = rx.App(
    style=styles.BASE_STYLES,
)  
app.add_page(
    index,
    title="SaulDev | aprendiendo a programar dia a dia",
    description="Hola mi nombre es Saul Orellana, soy un desarrollador full-stack junior, me gusta aprender cosas nuevas y compartir lo que aprendo, en este blog encontraras tutoriales de programacion, desarrollo web, desarrollo movil, desarrollo de videojuegos, y mucho mas, espero que te guste.",
    image="avatar.jpg"
)
app.compile()
    