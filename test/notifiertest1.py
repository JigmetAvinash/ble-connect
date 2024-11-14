from win10toast import ToastNotifier

toast = ToastNotifier()

toast.show_toast(
    "Your system was unlocked using your bluetooth device",
    "Your device (devicename) was used to unlock your device :P",
    duration=20,
    icon_path="icon.ico",
    threaded=True,
)
