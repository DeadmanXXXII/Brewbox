import os
from utils.terminal_output import print_green, print_red

def fingerprint(target):
    print(f"[+] Fingerprinting {target} as macOS...")
    result = os.system(f"curl -s -I http://{target} | grep -i 'Darwin\\|Macintosh\\|Safari'")
    if result == 0:
        print_green(f"[+] macOS detected on {target}")
    else:
        print_red(f"[-] Not a macOS system at {target}")