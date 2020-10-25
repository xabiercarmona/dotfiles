#!/bin/bash

##### PACMAN INSTALLATION FUNCTION #####

function pacman_install(){
    if pacman -Qi $1 &> /dev/null; then
        show_message "The package "$1" in already installed" 3
    else
        show_message "Installing package "$1"..." 3
        sudo pacman -S --noconfirm --needed $1
    fi
}

function show_message(){
    tput setaf $2
    echo $1
    tput sgr0
}

function temporal_message(){
    tput setaf $2
    echo -en $1
    tput sgr0
}
