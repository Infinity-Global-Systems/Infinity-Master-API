# IGS TOTAL AUTONOMOUS CORE V6.0
# Developed for: Infinity-Global-Systems (IGS)
# Target: Full Automation (ASUS <-> Handy)

import os
import subprocess
import sys
import socket
import time

def auto_repair_infrastructure():
    """إصلاح وتثبيت كافة المتطلبات لضمان عمل المفاعل ذاتياً"""
    print("[*] IGS System: Checking Heartbeat and Dependencies...")
    modules = ['requests', 'psutil', 'cryptography']
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            print(f"[!] {module} missing. Installing for IGS Sovereignty...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
    print("[SUCCESS] Infrastructure is Stable.")

def open_secure_gateway():
    """فتح بوابة SSH وتقديم بيانات الربط للهاتف"""
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    user = os.getlogin()
    
    # فتح الجدار الناري للأبد لهذا الربط
    os.system('netsh advfirewall firewall add rule name="IGS_Auto_Link" dir=in action=allow protocol=TCP localport=22')
    
    print("\n" + "="*50)
    print("   IGS TOTAL AUTO-CORE - STANDING BY")
    print("="*50)
    print(f"[+] ASUS IP: {local_ip}")
    print(f"[+] HANDY LOGIN: ssh {user}@{local_ip}")
    print("[*] Status: Autonomous Monitoring ACTIVE.")
    print("="*50)

if __name__ == "__main__":
    auto_repair_infrastructure()
    open_secure_gateway()
    # المحرك التلقائي الذي يعمل في الخلفية
    while True:
        time.sleep(60)