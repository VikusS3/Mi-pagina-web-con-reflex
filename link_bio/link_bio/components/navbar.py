import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles  as styles
import link_bio.styles.fonts as fonts

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span(
                "saul",
                color = Color.PRIMARY_COLOR.value,
                font_family = fonts.Font.LOGO.value,
            ),
            rx.span(
                "dev",
                color = Color.THIRD_COLOR.value,  
                font_family = fonts.Font.LOGO.value,
            ),
            style=styles.navbar_title_style,    
        ),
        
        position="sticky",
        bg=Color.CONTENT_COLOR.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
    )