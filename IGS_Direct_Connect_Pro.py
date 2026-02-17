# IGS DIRECT CONNECT PRO V4.0
# Developed for: Infinity (Ya Abqari)
# Function: Resolving SSH Connection & IP Discovery

import socket
import os
import subprocess

def fix_ssh_firewall():
    print("[*] IGS Shield: Opening Firewall Port 22 for Handy Access...")
    # أمر لفتح المنفذ 22 في جدار حماية ويندوز تلقائياً
    cmd = 'netsh advfirewall firewall add rule name="IGS_SSH_Handshake" dir=in action=allow protocol=TCP localport=22'
    os.system(cmd)
    print("[SUCCESS] Firewall configured for Direct Link.")

def get_sovereign_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

if __name__ == "__main__":
    print("="*60)
    print("   IGS DIRECT CONNECT - REPAIRING THE BRIDGE")
    print("="*60)
    fix_ssh_fireshake()
    my_ip = get_sovereign_ip()
    print(f"\n[!] INSTRUCTION FOR HANDY (Termux):")
    print(f"    ssh your_windows_user@{my_ip}")
    print("\n[STATUS] Waiting for Handy-to-ASUS Signal...")