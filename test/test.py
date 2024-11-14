import ctypes
import time
user32 = ctypes.windll.User32
time.sleep(5)
#
# print(user32.GetForegroundWindow())
#
while True:
    if (user32.GetForegroundWindow() % 10 == 0):
        print('Locked')
        print(time.localtime())
    # 10553666 - return code for unlocked workstation1
    # 0 - return code for locked workstation1
    #
    # 132782 - return code for unlocked workstation2
    # 67370 -  return code for locked workstation2
    #
    # 3216806 - return code for unlocked workstation3
    # 1901390 - return code for locked workstation3
    #
    # 197944 - return code for unlocked workstation4
    # 0 -  return code for locked workstation4

