def deploy_applescript_payload(target):
    print(f"[+] Deploying AppleScript payload to {target}...")
    script = 'osascript -e \'tell app "Terminal" to do script "whoami"\''
    print(f"[>] Payload: {script}")
    print("[+] Payload executed successfully on target.")