#Qtile widgets

from libqtile import widget
from settings.theme import colors
from settings.keys import terminal

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

icon = lambda fg='text', bg='dark', fontsize=14, text="?", padding=2: widget.TextBox(
    **base(fg, bg),
    fontsize=fontsize,
    text=text,
    padding=padding
)

workspaces = lambda: [
    separator(),
    widget.GroupBox(
        **base(fg='light'),
        font='UbuntuMono Nerd Font',
        fontsize=16,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=colors['active'],
        inactive=colors['inactive'],
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=colors['urgent'],
        this_current_screen_border=colors['focus'],
        this_screen_border=colors['grey'],
        other_current_screen_border=colors['dark'],
        other_screen_border=colors['dark'],
        disable_drag=True
    ),
    separator(),
    widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
    separator(),
]

primary_widgets = [
    *workspaces(),
    separator(),

    #Packman icon
    powerline('color5', 'dark'),
    icon(bg="color5", text=' '), # Icon: nf-fa-download
    widget.Pacman(**base(bg='color5'),
        mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
        update_interval=1800),

    #Net usage
    powerline('color4', 'color5'),
    #Net usage widget
    icon(bg="color4", text=' '),  # Icon: nf-fa-feed
    widget.Net(**base(bg='color4'),
        mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('nm-connection-editor')},
        format="{up} ↑↓{down}"),

    #Cput/RAM usage
    powerline('color3', 'color4'),
    #Cpu usage widget
    icon(bg="color3", text=' '),  # Icon: nf-mdi-speedometer
    widget.CPU(**base(bg='color3'),
        mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(terminal + ' -e htop')},
        format="{load_percent}%"),
    #RAM usage widget
    icon(bg="color3", text='溜'),  # Icon: nf-mdi-memory
    widget.Memory(**base(bg='color3'),
        mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(terminal + ' -e htop')}),

    #Layout
    powerline('color2', 'color3'),
    #Layout widget
    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.55),
    widget.CurrentLayout(**base(bg='color2')),

    #Clock
    powerline('color1', 'color2'),
    #Clock widget
    icon(bg="color1", text=' '), # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M:%S '),

    #Systray
    powerline('dark', 'color1'),
    widget.Systray(**base(bg='dark')),
]

secondary_widgets = [
    *workspaces(),
    separator(),

    powerline('color2', 'dark'),
    #Layout widget
    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.55),
    widget.CurrentLayout(**base(bg='color2')),

]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 12,
    'padding': 4,
}
extension_defaults = widget_defaults.copy()
