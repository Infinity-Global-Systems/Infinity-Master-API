# IGS AUTO-BRIDGE FINAL V5.0
# Developed for: Infinity-Global-Systems (IGS)
# Function: Self-Repair, Firewall Bypass, and Direct Handy Sync

import os
import subprocess
import sys
import socket

def igs_infrastructure_fix():
    print("[*] IGS System: Installing missing encryption and network modules...")
    modules = ['cryptography', 'requests', 'psutil']
    for module in modules:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])
    print("[SUCCESS] Infrastructure Repaired.")

def open_sovereign_gate():
    print("[*] IGS Shield: Opening Firewall Port 22 for Handy Access...")
    # فتح بوابات الويندوز للربط المباشر مع الهاتف
    os.system('netsh advfirewall firewall add rule name="IGS_Direct_Link" dir=in action=allow protocol=TCP localport=22')
    
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"\n[!] ASUS SOVEREIGN IP: {local_ip}")
    print(f"[!] USERNAME: {os.getlogin()}")
    print("-" * 30)
    print(f"COMMAND FOR HANDY (Termux): ssh {os.getlogin()}@{local_ip}")

if __name__ == "__main__":
    igs_infrastructure_fix()
    open_sovereign_gate()