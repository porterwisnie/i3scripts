#!/usr/bin/env python3
#THis is the gui for the displaymanager

#Script to check for outgoing HDMI connections in the HDMI-1 port
#Script toggles the connection on the non-native(?) display aka not eDPi-1
#Currently bound to F8 with i3wm

import subprocess

import re
def connection_status():

    status = subprocess.run('xrandr',stdout=subprocess.PIPE).stdout.decode('utf-8')

    s = re.findall(r'(HDMI-1 connected) (\d{3,4}x\d{3,4})',status,re.MULTILINE)

    if len(s) > 0:

        return 'Status:_Connected'

    else:

        return 'Status:_Disconnected'

def options_menu(connection):


    x = subprocess.run(str('zenity --list --title="Display_Manager"  --text='+ connection +' --column=Options Screen_Left Screen_Right Desktop_Mode Disconnect').split(),stdout=subprocess.PIPE)
    if x.returncode == 0:

        choice = re.sub('\\n','',x.stdout.decode('utf-8'))

        if choice == "Disconnect":

            subprocess.run('xrandr --output HDMI-1 --off'.split())

        elif choice == "Screen_Left":

            subprocess.run('xrandr --output eDP-1 --auto --output HDMI-1 --auto --left-of eDP-1'.split())
        
        elif choice == "Screen_Right":

            subprocess.run('xrandr --output eDP-1 --auto --output HDMI-1 --auto --right-of eDP-1'.split())

        elif choice == "Desktop_Mode":

            if connection == 'Status:_Connected':
            
                subprocess.run('xrandr --output eDP-1 --off'.split())

if __name__=="__main__":
   options_menu(connection_status()) 
