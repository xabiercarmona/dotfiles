#Qtile keys

from libqtile.config import Key
from libqtile.command import lazy
from settings.groups import groups

#Define mod keys (mod4 = windows key)
mod = "mod4"
alt = "mod1"
control = "control"
shift = "shift"
tab = "Tab"
intro = "Return"

#Define shortcuts
keys = [
    #Qtile
      Key([mod, control], "r", lazy.restart(), desc="Restart qtile"),
    #Kill window
      Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    #Layouts
      #Next layout
      Key([alt], tab, lazy.layout.next(), desc="Go to next"),
      Key([mod], tab, lazy.next_layout(), desc="Go to next layout"),
      Key([mod, shift], tab, lazy.prev_layout(), desc="Go to next layout"),

      #Go to window
      Key([alt], "Up", lazy.layout.up(), desc="Go to the top window"),
      Key([alt], "Down", lazy.layout.down(), desc="Go to the bottom window"),
      Key([alt], "Left", lazy.layout.left(), desc="Go to the left window"),
      Key([alt], "Right", lazy.layout.right(), desc="Go to the right window"),

      #Switch window
      Key([alt, control], "Up", lazy.layout.shuffle_up(), desc="Switch with the top window"),
      Key([alt, control], "Down", lazy.layout.shuffle_down(), desc="Switch with the bottom window"),
      Key([alt, control], "Left", lazy.layout.shuffle_left(), desc="Switch with the left window"),
      Key([alt, control], "Right", lazy.layout.shuffle_right(), desc="Switch with the right window"),

    #Menu
      #Fire rofi to start app
      Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Show app launcher"),
      #Fire rofi to toggle window
      Key([mod, shift], "r", lazy.spawn("rofi -show"), desc="Show window switcher"),

    #Apps
      Key([mod], intro, lazy.spawn("alacritty"), desc="Open terminal"),
      Key([mod], "r", lazy.spawn("google-chrome"), desc="Open browser"),
      Key([mod], "e", lazy.spawn("thunar"), desc="Open file explorer"),
      Key([mod], "s", lazy.spawn("scrot"), desc="Screenshot"),

    #Hardware
      #Audio (requires pactl)
      Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Volume up"),
      Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Volume down"),
      Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Toggle mute"),

      # Brightness (requires brightnessctl)
      Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Brightness up"),
      Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="Brightness down"),
]


# Set group modifiers
for i, group in enumerate(groups):
    groupNumber = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], groupNumber, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], groupNumber, lazy.window.togroup(group.name))
    ])
