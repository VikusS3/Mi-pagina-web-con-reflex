import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="vikusS3 dev", size="xl"),
        rx.text("@vikusS3dev"),
        rx.text("Hola ✌ MI NOMBRE ES VIKUS"),
        rx.text("""Soy tecnico en sistemas y programador con mas de un año de experiencia.
                Actualmente trabajo como freelance full-stack developer python, php y ASP.NET.
                Ademos de ser un apasionado por la tecnologia, me gusta mucho la musica y los videojuegos."""),
    )