import bluetooth
import wmi

def discover_nearby_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    return nearby_devices

def get_connected_bluetooth_devices():
    c = wmi.WMI()
    bluetooth_devices = c.query("SELECT * FROM Win32_PnPEntity WHERE Name LIKE '%Bluetooth%' AND Status='OK'")
    connected_devices = {device.Name for device in bluetooth_devices}
    return connected_devices

def main():
    nearby_devices = discover_nearby_devices()
    connected_devices = get_connected_bluetooth_devices()

    if nearby_devices:
        print("Nearby Bluetooth devices:")
        for addr, name in nearby_devices:
            connection_status = "Connected" if name in connected_devices else "Not Connected"
            print(f"  Device: {name} - Address: {addr} - Status: {connection_status}")
    else:
        print("No nearby devices found.")

if __name__ == "__main__":
    main()
