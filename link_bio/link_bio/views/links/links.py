import reflex as rx
from link_bio.components.link_button import link_button


def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "https://www.twitch.tv/vikussss3"),
        link_button("Youtube","https://www.youtube.com/channel/UCWTqiQVIA08vVTJhwy1SaDQ"),
        link_button("Linkedin","https://www.linkedin.com/in/felix-saul-orellana-contreras-971b042a6/"),
        link_button("Twitter", "https://twitter.com/Vikus3S"),
    )
    