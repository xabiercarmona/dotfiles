#Qtile theme

from os import path
import subprocess
import json

from settings.path import qtile_path

filename = "selected_theme.json"
themes_folder = "themes"
default_theme = "dracula"

def load_theme():
    theme = default_theme

    config = path.join(qtile_path, filename)
    if path.isfile(config):
        with open(config) as f:
            theme = json.load(f)["theme"]
    else:
        with open(config, "w") as f:
            f.write(f'{{"theme": "{theme}"}}\n')


    theme_file = path.join(qtile_path, themes_folder, f'{theme}.json')
    if not path.isfile(theme_file):
        raise Exception(f'"{theme_file}" does not exist')

    with open(path.join(theme_file)) as f:
        return json.load(f)


if __name__ == "settings.theme":
    colors = load_theme()
