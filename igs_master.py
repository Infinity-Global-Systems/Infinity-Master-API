import os
import time

# تعيين المسارات للعمل على الفلاشة حصراً
BASE_DIR = r'D:\IGS_GLOBAL_SYSTEMS'
LOG_FILE = os.path.join(BASE_DIR, 'system_log.txt')

def log_activity(message):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{time.ctime()}] {message}\n")

if __name__ == "__main__":
    print("--- [IGS-KEY] BOOTING FROM D: DRIVE ---")
    log_activity("System Initialized on External Key.")
    print(f"All operations are now anchored to: {BASE_DIR}")
