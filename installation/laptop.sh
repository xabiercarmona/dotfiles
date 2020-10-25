#!/bin/bash

#Include install scripst
source $(dirname "$0")/utils/install_functions.sh


##### LAPTOP STUFF INSTALLATION #####

list=(
#Bluetooth
puseaudio-bluetooth
bluez
bluez-libs
bluez-utils
blueberry
tlp
)


count=0

for name in "${list[@]}" ; do
    count=$[count+1]
    temporal_message "\rInstalling $name ($count/${#list[@]})\r" 6
    pacman_install $name
done

show_message "Enabling bluetooth ..." 3

sudo systemctl enable bluetooth.service
sudo systemctl start bluetooth.service
sudo sed -i 's/'#AutoEnable=false'/'AutoEnable=true'/g' /etc/bluetooth/main.conf

show_message "Enable tlp"
sudo systemctl enable tlp.service
