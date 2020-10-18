#Qtile mouse

from libqtile.config import Click, Drag
from libqtile.lazy import lazy
from settings.keys import mod

mouse = [
    #Drag mouse1 to move window and set floating
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    #Drag mouse3 to adjust window size
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    #Click mouse2 to toggle floating
    Click([mod], "Button2", lazy.window.toggle_floating()),
]
