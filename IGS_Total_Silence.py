# IGS TOTAL SILENCE V7.0
# [STEALTH-SHADOW-PROTOCOL]
# Auth: Infinity (Ya Abqari) - IGS Global

import os
import subprocess

def activate_silence():
    print("="*60)
    print("   IGS TOTAL SILENCE - [REMOVING VISIBILITY]")
    print("="*60)
    
    target_folder = r"D:\IGS_GLOBAL_SYSTEMS"
    
    if os.path.exists(target_folder):
        print(f"[*] Target identified: {target_folder}")
        # استخدام أمر السيادة (attrib) لحجب المجلد كمجلد نظام مخفي ومحمي
        # +h (hidden), +s (system), +r (read-only)
        try:
            subprocess.run(['attrib', '+h', '+s', '+r', target_folder], check=True)
            print("[SUCCESS] IGS Global Systems has entered STEALTH MODE.")
            print("[STATUS] Drive D: appears empty to unauthorized users.")
        except Exception as e:
            print(f"[ERROR] Sovereignty breach: {e}")
    else:
        print("[!] Target Folder not found. Check Path.")

if __name__ == "__main__":
    activate_silence()