# IGS PERSISTENT ORGANIZER & AUTO-FIX
# PURPOSE: PROFESSIONAL FILE ARCHITECTURE FOR IGS
# OWNER: INFINITY (YA ABQARI)

import os
import shutil

def activate_igs_structure():
    base_path = r"D:\IGS_GLOBAL_SYSTEMS"
    
    # 1. تعريف المجلدات المهنية المطلوبة
    folders = {
        "01_COMMAND_CENTER": "All core system controllers and dashboards",
        "02_PRODUCT_BUILD": "Source code for OMNIPOTENCE X-1",
        "03_SALES_MARKET": "Ads, HTML pages, and marketing bots",
        "04_FINANCE_VAULT": "Crypto receivers and invoice generators",
        "05_LICENSE_KEYS": "Database of generated keys for clients"
    }

    print("="*60)
    print("   IGS - AUTO-FIX & PROFESSIONAL ORGANIZATION")
    print("="*60)

    # 2. إنشاء الهيكل التنظيمي
    for folder, desc in folders.items():
        path = os.path.join(base_path, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"[+] Created: {folder} ({desc})")

    # 3. نقل الملفات إلى أماكنها الصحيحة (إذا كانت موجودة في المجلد الرئيسي)
    # ملاحظة: هذا الجزء سيقوم بترتيب مفاعلك تلقائياً
    mappings = {
        "IGS_Global_Dashboard.py": "01_COMMAND_CENTER",
        "IGS_Omnipotence_RT.py": "02_PRODUCT_BUILD",
        "IGS_Global_Ad.html": "03_SALES_MARKET",
        "IGS_Autopilot_Sales.py": "03_SALES_MARKET",
        "IGS_Crypto_Receiver.py": "04_FINANCE_VAULT",
        "IGS_Key_Generator.py": "05_LICENSE_KEYS"
    }

    for file, target_folder in mappings.items():
        src = os.path.join(base_path, "01_COMMAND_CENTER", file) # الموقع الحالي المحتمل
        dest = os.path.join(base_path, target_folder, file)
        
        if os.path.exists(src) and src != dest:
            shutil.move(src, dest)
            print(f"[➔] Moved {file} to {target_folder}")

    print("\n[SUCCESS] IGS PERSISTENT IS NOW PROFESSIONALLY ORGANIZED.")
    print("[!] Access your Command Center at: D:/IGS_GLOBAL_SYSTEMS/01_COMMAND_CENTER/")

if __name__ == "__main__":
    activate_igs_structure()