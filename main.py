# file: main.py
# auth: Jigmet Avinash Kumar (@JigmetAvinash on Github)
# desc: Helps in auto-unlocking of device when connected to a specific ble device
# $Id: jigmet $
# MIT License Acquired as of 2024 ©️

import pyautogui
import bluetooth
import time
import psutil
from win10toast import ToastNotifier
import keyboard
toaster = ToastNotifier()

## Program Run
print("Program run")
## Program Run End


## Gathering from resource file

Resourcefile = open("resource.txt", "r+")

print("Output of Read function is ")
txt = Resourcefile.readlines()
print(txt)

unwantedtext = "\n"
txt1 = []

for i in txt[1]:
    if i == unwantedtext:
        txt[1] = txt[1].strip(unwantedtext)
        print(txt)
for i in txt[2]:
    if i == unwantedtext:
        txt[2] = txt[2].strip(unwantedtext)
        print(txt)



##Unlock and Bluetooth Check function
namesInBle = []

def checkBleAndUnlockSys():
    nearby_devices = bluetooth.discover_devices(
        duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

    for addr, name in nearby_devices:
        try:
            namesInBle.append(name)
        except UnicodeEncodeError:
            print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))
    if txt[1] in namesInBle:
        keyboard.press_and_release('esc')
        time.sleep(3)
        pyautogui.write(txt[2], interval=0.25)
        print("Test apss")


while True:
    time.sleep(2)
    for proc in psutil.process_iter():
        if (proc.name() == "LogonUI.exe"):
            print("Locked")
            try:
                checkBleAndUnlockSys()
            finally:
                toaster.show_toast("Unlocked using BLEUNLOCK ",
                                "Your machine was unlocked using bluetooth device",
                                duration=10)

        
    

    


