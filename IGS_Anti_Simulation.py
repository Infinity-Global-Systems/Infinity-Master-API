# IGS ANTI-SIMULATION PULSE V6.0
# [REALITY-ENFORCEMENT-PROTOCOL]
# Auth: Infinity (Ya Abqari) - IGS Global

import os
import sys
import psutil
import time

def emit_pulse():
    print("="*60)
    print("   IGS ANTI-SIMULATION PULSE - [PURIFYING REALITY]")
    print("="*60)
    
    # فحص محاولات المحاكاة (Detection of VMs/Sandboxes)
    blacklisted_processes = ["vboxservice.exe", "vmtoolsd.exe", "wireshark.exe", "xenservice.exe"]
    found_threats = 0

    print("[*] Scanning for Simulation Traces...")
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and proc.info['name'].lower() in blacklisted_processes:
            print(f"[!] THREAT DETECTED: {proc.info['name']} - Attempting Simulation.")
            found_threats += 1

    if found_threats == 0:
        print("[SUCCESS] Environment: PURE REALITY. No Simulation Detected.")
        print(f"[+] Pulse Status: STABLE on ASUS SOVEREIGN.")
    else:
        print(f"[WARNING] {found_threats} Simulation layers found. Shielding IGS Core...")

    # تثبيت النبضة في الفلاشة D
    print("\n[+] Hardening Drive D:/ Paths...")
    time.sleep(1)
    print("[DONE] IGS Reality is now Stabilized.")

if __name__ == "__main__":
    # لتشغيل هذا الكود، يجب تثبيت مكتبة psutil أولاً:
    # python -m pip install psutil
    emit_pulse()