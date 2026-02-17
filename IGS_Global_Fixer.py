# IGS GLOBAL FIXER V15.0 - [AUTO-RECONSTRUCT]
# Designed for: Infinity (Ya Abqari)
# System: ASUS Sovereign + Drive D Integration

import os
import sys
import subprocess
import socket

def debug_and_reconstruct():
    print("="*60)
    print("   IGS AUTO-FIX - SYSTEM RECONSTRUCTION IN PROGRESS")
    print("="*60)
    
    # 1. تصحيح التبعيات (المكتبات التي ظهرت فيها أخطاء في صورك)
    modules = ['cryptography', 'requests', 'psutil', 'docker']
    for module in modules:
        try:
            __import__(module)
            print(f"[OK] {module} is stable.")
        except ImportError:
            print(f"[!] {module} missing. Forcing reconstruction...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

    # 2. فتح الجدار الناري (لحل مشكلة هاتفك Connection Timed Out)
    print("\n[*] Piercing Firewall for Handy Link...")
    os.system('netsh advfirewall firewall add rule name="IGS_Sovereign_Link" dir=in action=allow protocol=TCP localport=22')

    # 3. استخراج البيانات السيادية للربط
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f"\n[SUCCESS] Repair Complete.")
    print(f"[!] Target IP for Handy: {ip}")
    print(f"[!] Use this on Termux: ssh {os.getlogin()}@{ip}")

if __name__ == "__main__":
    debug_and_reconstruct()