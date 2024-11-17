import subprocess


def get_connected_audio_devices():
    cmd = 'Get-PnpDevice -class AudioEndpoint | Where-Object { $_.Status -eq "OK" } | Select-Object FriendlyName, Status'
    result = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True, text=True)

    if result.returncode == 0:
        print("Connected audio devices:")
        print(result.stdout)
    else:
        print("Failed to get connected audio devices.")
        print(result.stderr)


if __name__ == "__main__":
    get_connected_audio_devices()


