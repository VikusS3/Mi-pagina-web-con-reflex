import reflex as rx
from enum import Enum

#constants for the styles
MAX_WIDTH = "600px"

#Sizes
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM ="0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    
    
#styles

BASE_STYLES = {
    rx.Button:{
        "width": "100%",
        "height": "100%",
        "display":"block",
        "padding": Size.SMALL.value,
        "boder_radius": Size.SMALL.value,
    },
    rx.Link:{
        "text_decoration": "none",
        "_hover":{}
    }
}

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value,
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
)