#Qtile widgets

from libqtile import widget
from settings.theme import colors

base = lambda fg='text', bg='dark': {
    'foreground': colors[fg],
    'background': colors[bg]
}

separator = lambda: widget.Sep(**base(), linewidth=0, padding=5)

powerline = lambda fg="light", bg="dark": widget.TextBox(
   **base(fg, bg),
    text="", # Icon: nf-oct-triangle_left
    fontsize=37,
    padding=-2
)

icon = lambda fg='text', bg='dark', fontsize=16, text="?", padding=3: widget.TextBox(
    **base(fg, bg),
    fontsize=fontsize,
    text=text,
    padding=padding
)

primary_widgets = [

    widget.GroupBox(),
    widget.Prompt(),
    widget.WindowName(),
    widget.Chord(
        chords_colors={
            'launch': ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),

    #Systray
    widget.Systray(),

    #Packman icon
    powerline('color4', 'dark'),
    icon(bg="color4", text=' '), # Icon: nf-fa-download
    widget.Pacman(**base(bg='color4'), update_interval=1800),

    #Net/Cpu/RAM usage
    powerline('color3', 'color4'),
    #Net usage widget
    #icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    icon(bg="color3", text='',fontsize=10, padding=0),  # Icon: nf-fa-long_arrow_up
    icon(bg="color3", text=' ',fontsize=10, padding=0),  # Icon: nf-fa-long_arrow_down
    widget.Net(**base(bg='color3'), interface="enp0s3"),
    #Cpu usage widget
    icon(bg="color3", text=' 龍'),  # Icon: nf-mdi-speedometer
    widget.CPU(**base(bg='color3')),
    #RAM usage widget
    icon(bg="color3", text=' '),  # Icon: nf-mdi-memory
    widget.Memory(**base(bg='color3')),

    #Layout
    powerline('color2', 'color3'),
    #Layout widget
    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
    widget.CurrentLayout(**base(bg='color2')),

    #Clock
    powerline('color1', 'color2'),
    #Clock widget
    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M:%S '),
]

secondary_widgets = [
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 12,
    'padding': 4,
}
extension_defaults = widget_defaults.copy()
