# file: inquiry.py
# auth: Jigmet Avinash Kumar (@JigmetAvinash on Github)
# desc: Helps in auto-unlocking of device when connected to a specific ble device
# $Id: inquiry.py 401 2006-05-05 19:07:48Z jigmet $
#

import bluetooth
import time
import ctypes
from win10toast import ToastNotifier
import keyboard

print("Program run on" + time.localtime())

namesInBle = []

nearby_devices = bluetooth.discover_devices(
    duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    try:
        namesInBle.append(name)
    except UnicodeEncodeError:
        print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))

def checkBle():
    


