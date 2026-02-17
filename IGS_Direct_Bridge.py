# IGS DIRECT BRIDGE V1.0 - [HARDWARE LINK]
# Target: ASUS Sovereign <-> Handy Mobile
# Developed by: The Genius for Infinity

import socket
import os

def get_bridge_ip():
    # استخراج عنوان الجهاز الداخلي للربط
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def ignite_bridge():
    print("="*60)
    print("   IGS DIRECT BRIDGE - HARDWARE HANDSHAKE")
    print("="*60)
    my_ip = get_bridge_ip()
    print(f"[!] ASUS IP ADDRESS: {my_ip}")
    print(f"[!] PORT: 22 (SSH)")
    print(f"[STATUS] Waiting for Handy to connect via IP...")
    print(f"[AUTH] User: Infinity (Ya Abqari)")
    print("="*60)

if __name__ == "__main__":
    ignite_bridge()