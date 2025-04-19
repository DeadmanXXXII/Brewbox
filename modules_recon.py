import os
from utils.terminal_output import print_green, print_red

def recon(target):
    print(f"[+] Performing macOS recon on {target}...")
    result = os.system(f"avahi-browse -a | grep apple")
    if result == 0:
        print_green(f"[+] Found Apple device at {target}")
    else:
        print_red(f"[-] No Apple device found at {target}")