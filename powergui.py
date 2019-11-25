#!/usr/bin/env python3
import re
import subprocess

x = subprocess.run(str('zenity --list --title="Poweroff" --text="Power_Options" --column=Option Shutdown Reboot Cancel').split(),stdout=subprocess.PIPE)
if x.returncode == 0:

    choice = re.sub('\\n','',x.stdout.decode('utf-8'))
    
    if choice == "Shutdown":

        subprocess.run(['shutdown','-h','now'])

    elif choice == "Reboot":

        subprocess.run(['restart','-r'])


