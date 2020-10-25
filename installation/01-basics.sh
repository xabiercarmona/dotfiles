#!/bin/bash

#Include install scripst
source $(dirname "$0")/utils/install_functions.sh


##### ENVIRONMENT INSTALLATION #####

list=(
#Xorg
xorg-server
xorg-apps
xorg-xinit
#LightDM
lightdm
lightdm-webkit2-greeter
lightdm-webkit-theme-litarvan
#Qtile
qtile
#Essentials
alacritty
bash-completion
rofi
which
python-psutil
htop
git
)


count=0

for name in "${list[@]}" ; do
    count=$[count+1]
    temporal_message "\rInstalling $name ($count/${#list[@]})\r" 6
    pacman_install $name
done


#Backup existing files
sudo cp /etc/lightdm/lightdm.conf{,.old}
sudo cp /etc/lightdm/lightdm-webkit2-greeter.conf{,.old}

show_message "Copying lightdm configuration ..." 5

sudo cp $(dirname "$0")/lightdm/lightdm.conf /etc/lightdm/lightdm.conf
sudo cp $(dirname "$0")/lightdm/greeter.conf /etc/lightdm/lightdm-webkit2-greeter.conf

show_message "Enabling lightdm ..." 5

sudo systemctl enable lightdm.service -f

show_message "You got now basic desktop functionallity. Please reboot" 5
