#Qtile groups

from libqtile.config import Group
# Name the groups and assing numbers to them.
# Can use icons from https://www.nerdfonts.com/cheat-sheet (Nerd Font required)
groups = [Group(i) for i in [
    "MAIN", "DEV", "</>", "WWW", "FILES",
]]
