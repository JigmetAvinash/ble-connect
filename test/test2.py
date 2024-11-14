import subprocess
import time
time.sleep(5)
process_name = 'LogonUI.exe'
callall = 'TASKLIST'
outputall = subprocess.check_output(callall)
outputstringall = str(outputall)
while True:
    if process_name in outputstringall:
        print("Locked.")
    time.sleep(1)
    print("Program Run Success")
