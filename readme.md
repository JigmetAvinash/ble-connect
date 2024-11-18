

# BLEUnlock

## Description
BLEUnlock helps in auto-unlocking your Windows device when connected to a specific Bluetooth device. This project uses Bluetooth to detect the presence of your device and automatically unlocks your computer.

## Features
- Automatically unlocks your Windows machine when a specific Bluetooth device is in range.
- Uses Bluetooth for device detection.
- Simple setup process.
- Provides notifications upon unlocking.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JigmetAvinash/BLEUnlock.git
   cd BLEUnlock


2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the setup script:**
   ```bash
   python setup.py
   ```

## Usage

1. **Run the main script:**
   ```bash
   python main.py
   ```

2. **Ensure your Bluetooth device is in range:**
   The script will automatically detect your Bluetooth device and unlock your machine.

## Setup Script

The `setup.py` script will:
- Install the required dependencies from `requirements.txt`.
- Prompt you to enter the name of your Bluetooth device and your password.
- Save these credentials in a plain text file (`resource.txt`).

## Main Script

The `main.py` script will:
- Continuously check for the presence of your Bluetooth device.
- Unlock your machine by simulating key presses when the device is detected.

## Warnings
- **Security:** The password is stored in plain text. Ensure your `resource.txt` file is kept secure.
- **Bluetooth:** Make sure your Bluetooth device name is entered exactly as it appears in the control panel.
- **Do not remove resource.txt or any test** 

## Author
- **Jigmet Avinash Kumar** (@JigmetAvinash on Github)

## To-Do List
- [ ] Improve security by encrypting the password.
- [ ] Add support for multiple Bluetooth devices.
- [ ] Implement a graphical user interface (GUI) for easier setup.
- [ ] Add more customization options for notifications.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

