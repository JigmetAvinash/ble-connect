import psutil
import pyautogui
import bluetooth
import time 
import ctypes
from win10toast import ToastNotifier

lockedStatus = False

while True:
    time.sleep(5)
    for proc in psutil.process_iter():
        if (proc.name() == "LogonUI.exe"):
            print("Locked")
            lockedStatus = True
    print("Program ifLocked Run Success")


