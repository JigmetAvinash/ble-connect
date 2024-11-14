import psutil

while True:
    for proc in psutil.process_iter():
        if (proc.name() == "LogonUI.exe"):
            print("Locked")
    print("Program Run Success")
