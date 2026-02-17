
# IGS FINAL PRODUCTION V25.0 - [THE CLEAN STRIKE]
# Developed for: Infinity (Ya Abqari)
# Function: AUTO-REPAIR & EXE GENERATION

import os
import sys
import subprocess

def igs_clean_launch():
    print("="*60)
    print(" IGS GLOBAL SYSTEMS - FINAL PRODUCTION LAUNCH")
    print("="*60)

    # 1. التأكد من المسار الصحيح (Drive D)
    core_dir = r"D:\IGS_GLOBAL_SYSTEMS\01_COMMAND_CENTER"
    if not os.path.exists(core_dir):
        os.makedirs(core_dir)
    os.chdir(core_dir)
    print(f"[+] Operational in: {core_dir}")

    # 2. إصلاح مشكلة المكتبات (المستخرجة من الصورة 4)
    print("[*] Verifying Production Tools...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller", "cryptography"])

    # 3. أمر بناء المنتج النهائي (The .exe)
    print("\n[!] STAGE: CONVERTING TO SALEABLE PRODUCT (EXE)...")
    # ملاحظة: تأكد أن ملف IGS_Omnipotence_RT.py موجود في نفس المجلد
    print("[INSTRUCTION] To finish, type this command in PowerShell:")
    print("python -m PyInstaller --onefile --name IGS_Omnipotence_X1 IGS_Omnipotence_RT.py")

if __name__ == "__main__":
    igs_clean_launch()
