import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size


def links() -> rx.Component:
    return rx.vstack(
        title(
          "Mis Redes Sociales"  
        ),
        link_button("Twitch",
                    "Directos de vez en cuando",
                    "https://www.twitch.tv/vikussss3"),
        link_button("Youtube", 
                    "Guias y Tutoriales",
                    "https://www.youtube.com/channel/UCWTqiQVIA08vVTJhwy1SaDQ"),
        link_button("Linkedin", 
                    "Informacion profesional",
                    "https://www.linkedin.com/in/felix-saul-orellana-contreras-971b042a6/"),
        link_button("Twitter", 
                    "Actualizacion de estados y publicaciones",
                    "https://twitter.com/Vikus3S"),
        width="100%",
        spacing=Size.DEFAULT.value,
    )
