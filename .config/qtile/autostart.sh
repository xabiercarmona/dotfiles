#!/bin/sh

#Battery icon
cbatticon -u 5 &
#Volume
volumeicon &
#Network
nm-applet&
#USB connection
udiskie -t &
#Wallpaper
nitrogen --restore &
