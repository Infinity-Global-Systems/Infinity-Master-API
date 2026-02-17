# IGS GLOBAL REPAIR & RECONSTRUCT V2.0
# Target: Repairing Path, PIP, and Environment for Infinity (Ya Abqari)

import os
import subprocess
import sys

def igs_auto_fix():
    print("="*60)
    print("   IGS AUTO-FIX : REPAIRING ASUS SOVEREIGN SYSTEM")
    print("="*60)

    # 1. الانتقال الإجباري للفلاشة D (حل مشكلة الصورة 1 و 5)
    core_path = r"D:\IGS_GLOBAL_SYSTEMS\01_COMMAND_CENTER"
    if not os.path.exists(core_path):
        os.makedirs(core_path)
    os.chdir(core_path)
    print(f"[+] Moved to Secure Core: {core_path}")

    # 2. تحديث PIP وتثبيت أدوات الإنتاج (حل مشكلة الصورة 6)
    print("[*] Updating Sovereign Tools...")
    tools = ['pyinstaller', 'cryptography', 'requests']
    for tool in tools:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", tool])
            print(f"[OK] {tool} is ready for production.")
        except:
            print(f"[!] Error installing {tool}.")

    # 3. أمر بناء المنتج النهائي (OMNIPOTENCE X-1)
    print("\n[*] Ready to Freeze OMNIPOTENCE X-1...")
    print(f"[INSTRUCTION] To build the EXE, run this exactly:")
    print(f"python -m PyInstaller --onefile IGS_Omnipotence_RT.py")

if __name__ == "__main__":
    igs_auto_fix()