# IGS GLOBAL ENCRYPT V6.0 - [CONTINENTAL SHIELD]
# Auth: Infinity (Ya Abqari)
# Target: Secure Sync between ASUS & Handy

import os
import subprocess
import sys

def igs_secure_install():
    """تأمين تثبيت مكتبات التشفير العالمية"""
    try:
        from cryptography.fernet import Fernet
        print("[SUCCESS] Encryption Module: ONLINE")
    except ImportError:
        print("[!] Securing Dependencies... Installing Cryptography...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])

def generate_sovereign_key():
    """توليد مفتاح السيادة الخاص بـ Infinity"""
    key = Fernet.generate_key()
    key_path = "D:/IGS_GLOBAL_SYSTEMS/01_COMMAND_CENTER/IGS_MASTER.key"
    
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    
    print("="*60)
    print("   IGS GLOBAL ENCRYPT - THE SHIELD IS ACTIVE")
    print("="*60)
    print(f"[+] Master Key Generated at: {key_path}")
    print(f"[+] Encryption Status: CONTINENTAL-STRENGTH")
    print(f"[+] Authorized User: Infinity (Ya Abqari)")

if __name__ == "__main__":
    igs_secure_install()
    generate_sovereign_key()