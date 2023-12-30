import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
import link_bio.constants as constants


def links() -> rx.Component:
    return rx.vstack(
        title(
          "Mis Redes Sociales"  
        ),
        link_button("Twitch",
                    "Directos de vez en cuando",
                    "icons/twitch.svg",
                    constants.TWITCH_URL),
        link_button("Youtube", 
                    "Guias y Tutoriales",
                    "icons/youtube.svg",
                     constants.YOUTUBE_URL),
        link_button("Linkedin", 
                    "Informacion profesional",
                    "icons/linkedin.svg",
                    constants.LINKEDIN_URL),
        link_button("Twitter", 
                    "Actualizacion de estados y publicaciones",
                    "icons/x-twitter.svg",
                    constants.TWITTER_X_URL),
        
        title(
          "Contacto"  
        ),
        link_button("Email",
                    "¿Quieres colaborar conmigo?",
                    "icons/envelope-solid.svg",
                    f"mailto:{constants.MY_EMAIL}"),
        link_button("MyEmailEducation", 
                     constants.MY_EMAIL_EDU,
                     "icons/school-solid.svg",
                     f"mailto:{constants.MY_EMAIL_EDU}"
                    ),
        
        
        width="100%",
        spacing=Size.DEFAULT.value,
    )
