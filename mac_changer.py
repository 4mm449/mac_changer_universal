import subprocess
import platform

input("Welcome to MAC address changer by 4im\nPress return to continue...")

interface = input("Please enter the name of the interface you want to change the MAC Address for:\n")
new_mac = input("Please enter new mac:\n")

print("changing mac address for " + interface + " to " + new_mac)

if platform.system() == "Windows":
    subprocess.call(["netsh", "interface", "set", "interface", interface, "newmac=" + new_mac])
elif platform.system() == "Darwin":
    subprocess.call(["sudo", "ifconfig", interface, "ether", new_mac])
else:
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

subprocess.call(["ifconfig", interface])