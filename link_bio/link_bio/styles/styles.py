import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

#constants for the styles
MAX_WIDTH = "600px"

#Sizes
class Size(Enum):
    ZERO = "0px !important",
    SMALL = "0.5em"
    MEDIUM ="0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    
    
#styles

BASE_STYLES = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND_COLOR.value,
    
    rx.Button:{
        "width": "100%",
        "height": "100%",
        "display":"block",
        "padding": Size.SMALL.value,
        "boder_radius": Size.SMALL.value,
        "color": TextColor.BODY_COLOR.value,
        "background_color": Color.SECONDARY_COLOR.value,
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
)

title_style = dict(
    width = "100%",
    font_family = Font.TITLE.value,
    padding_top = Size.DEFAULT.value,
    color = TextColor.HEADER_COLOR.value,
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    font_family=Font.TITLE.value,
    color=TextColor.HEADER_COLOR.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    font_family=Font.DEFAULT.value,
    Color=TextColor.BODY_COLOR.value,
)