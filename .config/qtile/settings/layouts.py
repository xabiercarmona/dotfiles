from libqtile import layout

# Set allowed layouts, and add a toggle key

#Configuration for layout window
layout_conf = {
#    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 4
}

#Define available layouts
layouts = [
    #All windows max size
    layout.Max(),
    #Master and slave stack
    layout.MonadTall(),
    #All windows almost equal distribution
    layout.RatioTile(),
    #All windows max with task
    layout.TreeTab(),
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
