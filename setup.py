import time
import subprocess
credentialFile = open("resource.txt", "a")
credentialList = []


def print_big_letters(text):
    letters = {
        'A': ['  ▓  ', ' ▓ ▓ ', '▓▓▓▓▓', '▓   ▓', '▓   ▓'],
        'B': ['▓▓▓▓ ', '▓   ▓', '▓▓▓▓ ', '▓   ▓', '▓▓▓▓ '],
        'C': [' ▓▓▓ ', '▓   ▓', '▓    ', '▓   ▓', ' ▓▓▓ '],
        'D': ['▓▓▓▓ ', '▓   ▓', '▓   ▓', '▓   ▓', '▓▓▓▓ '],
        'E': ['▓▓▓▓▓', '▓    ', '▓▓▓▓▓', '▓    ', '▓▓▓▓▓'],
        'F': ['▓▓▓▓▓', '▓    ', '▓▓▓▓ ', '▓    ', '▓    '],
        'G': [' ▓▓▓ ', '▓    ', '▓  ▓▓', '▓   ▓', ' ▓▓▓ '],
        'H': ['▓   ▓', '▓   ▓', '▓▓▓▓▓', '▓   ▓', '▓   ▓'],
        'I': [' ▓▓▓ ', '  ▓  ', '  ▓  ', '  ▓  ', ' ▓▓▓ '],
        'J': ['  ▓▓▓', '   ▓ ', '   ▓ ', '▓  ▓ ', ' ▓▓  '],
        'K': ['▓   ▓', '▓  ▓ ', '▓▓▓  ', '▓  ▓ ', '▓   ▓'],
        'L': ['▓    ', '▓    ', '▓    ', '▓    ', '▓▓▓▓▓'],
        'M': ['▓   ▓', '▓▓ ▓▓', '▓ ▓ ▓', '▓   ▓', '▓   ▓'],
        'N': ['▓   ▓', '▓▓  ▓', '▓ ▓ ▓', '▓  ▓▓', '▓   ▓'],
        'O': [' ▓▓▓ ', '▓   ▓', '▓   ▓', '▓   ▓', ' ▓▓▓ '],
        'P': ['▓▓▓▓ ', '▓   ▓', '▓▓▓▓ ', '▓    ', '▓    '],
        'Q': [' ▓▓▓ ', '▓   ▓', '▓   ▓', '▓  ▓▓', ' ▓▓▓▓'],
        'R': ['▓▓▓▓ ', '▓   ▓', '▓▓▓▓ ', '▓  ▓ ', '▓   ▓'],
        'S': [' ▓▓▓ ', '▓    ', ' ▓▓▓ ', '    ▓', ' ▓▓▓ '],
        'T': ['▓▓▓▓▓', '  ▓  ', '  ▓  ', '  ▓  ', '  ▓  '],
        'U': ['▓   ▓', '▓   ▓', '▓   ▓', '▓   ▓', ' ▓▓▓ '],
        'V': ['▓   ▓', '▓   ▓', '▓   ▓', ' ▓ ▓ ', '  ▓  '],
        'W': ['▓   ▓', '▓   ▓', '▓ ▓ ▓', '▓▓ ▓▓', '▓   ▓'],
        'X': ['▓   ▓', ' ▓ ▓ ', '  ▓  ', ' ▓ ▓ ', '▓   ▓'],
        'Y': ['▓   ▓', ' ▓ ▓ ', '  ▓  ', '  ▓  ', '  ▓  '],
        'Z': ['▓▓▓▓▓', '   ▓ ', '  ▓  ', ' ▓   ', '▓▓▓▓▓'],
        ' ': ['     ', '     ', '     ', '     ', '     ']
    }
    for i in range(25):
        print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")

    for i in range(5):
        time.sleep(0.1)
        for char in text:

            print(letters[char][i], end='  ')
        time.sleep(0.5)
        print()


print_big_letters("BLEUNLOCK")
time.sleep(0.1)
print("©️ 2024, JigmetAvinash @ Github // contact.chopcode@proton.me ")
time.sleep(0.1)
print("This program helps you unlock your windows machine as soon as your bluetooth device is in range of your computer. It uses bluetooth. For issues please refer to github BleUnlock/JigmetAvinash")
time.sleep(0.1)
print("-->version 0.1.4")
time.sleep(0.1)
print("-->This is a setup.py file only for setup")


def setup():
    for i in range(3):
        print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    try:
        bleDevName = str(input(
            "What is the name of your Bluetooth Device? (Make sure it is AS IS in the control panel))"))
        print("THIS WILL BE SAVED IN PLAIN TEXT, REFER TO README.MD ON GITHUB")
        password = str(input(
            "What is your password? (Please type as you type while unlocking your machine)"))
        credentialList.append(bleDevName)
        credentialList.append(password)
        
        credentialFile.write(bleDevName + "\n")
        credentialFile.write(password + "\n")
        credentialFile.close()

        for i in range(3):
            print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
        print(" Please now run main.py! SETUP SUCCESSFUL!")
    except:
        print("Error, file couldn't run. Please refer to source code or post an inssue on the github page")
    try:
        subprocess.run(["python", "main.py"])
    except:
        print("Error in runnning shell, please run \n python main.py \n manually")


setup()
