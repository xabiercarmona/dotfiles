#!/bin/bash

#Include install scripst
source $(dirname "$0")/utils/install_functions.sh


##### UTILITIES INSTALLATION #####

list=(
#Screen
arandr
nitrogen
#Fonts
ttf-dejavu
#File manager
thunar
thunar-archive-plugin
thunar-volman
#Image viewer
feh
#Screenshots
scrot
#Audio
pulseaudio
pulseaudio-alsa
pavucontrol
alsa-firmware
alsa-lib
alsa-plugins
alsa-utils
gstreamer
#Video
vlc
#Unpack
zip
unzip
unrar
)


count=0

for name in "${list[@]}" ; do
    count=$[count+1]
    temporal_message "\rInstalling $name ($count/${#list[@]})\r" 6
    pacman_install $name
done
