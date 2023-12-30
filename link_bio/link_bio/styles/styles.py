import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font,FontWeight

#constants for the styles
MAX_WIDTH = "600px"


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

#Sizes
class Size(Enum):
    ZERO = "0px !important",
    SMALL = "0.5em"
    MEDIUM ="0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    
    
#styles

BASE_STYLES = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND_COLOR.value,
    
    rx.Button:{
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "boder_radius": Size.SMALL.value,
        "color": TextColor.BODY_COLOR.value,
        "background_color": Color.SECONDARY_COLOR.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover":{
            "background_color": Color.PRIMARY_COLOR.value,
            "color": TextColor.HEADER_COLOR.value,
        }
    },
    rx.Link:{
        "text_decoration": "none",
        "_hover":{}
    }
}

navbar_title_style = dict(
    font_size=Size.LARGE.value,
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
)

title_style = dict(
    width = "100%",
    font_family = Font.TITLE.value,
    font_weight = FontWeight.MEDIUM.value,
    padding_top = Size.DEFAULT.value,
    color = TextColor.HEADER_COLOR.value,
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    font_family=Font.TITLE.value,
    color=TextColor.HEADER_COLOR.value,
    font_weight=FontWeight.MEDIUM.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    font_weight=FontWeight.LIGHT.value,
    font_family=Font.DEFAULT.value,
    Color=TextColor.BODY_COLOR.value,
)