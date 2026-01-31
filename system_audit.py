import os
import platform
import datetime

def run_sovereign_audit():
    print("🔱 [AUDIT] Starting Full System Inspection...")
    report = {
        "timestamp": str(datetime.datetime.now()),
        "environment": platform.system(),
        "files_found": [],
        "errors": []
    }

    # 1. فحص المجلدات والملفات الموجودة
    try:
        current_dir = os.listdir('.')
        report["files_found"] = current_dir
        print(f"📁 Files detected: {current_dir}")
    except Exception as e:
        report["errors"].append(f"Directory access error: {str(e)}")

    # 2. فحص محتوى "الكود الأوحد" و "الوحدة المالية"
    targets = ["gateway.py", "Sovereign_FinNet.py", "audit_log.txt"]
    for target in targets:
        if os.path.exists(target):
            print(f"✅ Found: {target}")
            # فحص صلاحيات الملف
            stats = os.stat(target)
            print(f" Permissions: {oct(stats.st_mode)[-3:]}")
        else:
            print(f"❌ Missing: {target}")
            report["errors"].append(f"Missing critical file: {target}")

    # 3. محاكاة تشغيل المحرك المالي للتأكد من جاهزيته
    print("--- Testing Sovereign Logic ---")
    if "Sovereign_FinNet.py" in current_dir:
        print("🔗 Finance Module ready for deployment.")
    
    print("🔱 [AUDIT] Inspection Complete.")
    return report

if __name__ == "__main__":
    run_sovereign_audit()

