from libqtile import layout
from settings.theme import colors

# Set allowed layouts, and add a toggle key

#Configuration for layout window
layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 2,
    'margin': 4
}

#Define available layouts
layouts = [
    #All windows max size
    layout.Max(),
    #Master and slave stack
    layout.MonadTall(**layout_conf),
    #All windows almost equal distribution
    layout.Bsp(**layout_conf),
    #All windows max with task
    layout.TreeTab(**layout_conf,

        font='UbuntuMono Nerd Font',
        fontsize=15,
        section_fontsize=16,
        section_left = 6,
        previous_on_rm='True',
        sections=['Open tabs'],
        active_bg=colors['focus'],
        active_fg=colors['light'],
        inactive_bg=colors['dark'],
        inactive_fg=colors['inactive']),
]

floating_layout = layout.Floating(
    float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
        {'wmclass': 'confirm'},
        {'wmclass': 'dialog'},
        {'wmclass': 'download'},
        {'wmclass': 'error'},
        {'wmclass': 'file_progress'},
        {'wmclass': 'notification'},
        {'wmclass': 'splash'},
        {'wmclass': 'toolbar'},
        {'wmclass': 'confirmreset'},  # gitk
        {'wmclass': 'makebranch'},  # gitk
        {'wmclass': 'maketag'},  # gitk
        {'wname': 'branchdialog'},  # gitk
        {'wname': 'pinentry'},  # GPG key password entry
        {'wmclass': 'ssh-askpass'},  # ssh-askpass
    ]
)
