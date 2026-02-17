
# -*- coding: utf-8 -*-
import os, psutil, time, threading
from cryptography.fernet import Fernet
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- المسارات السيادية لـ IGS ---
BASE_PATH = r"E:\IGS_CYBER_PRIME"
VAULT_PATH = os.path.join(BASE_PATH, "IGS_ENCRYPTED_VAULT")
KEY_PATH = os.path.join(BASE_PATH, "IGS_MASTER.key")
os.makedirs(VAULT_PATH, exist_ok=True)

class IGS_Final_Sovereign:
    def __init__(self):
        self.key = self.get_key()
        self.cipher = Fernet(self.key)
        print("🏛️ IGS OMNI-CORE: SYSTEM IS LIVE & ARMED 100%")
        print(f"🛡️ MONITORING: {BASE_PATH}")

    def get_key(self):
        if not os.path.exists(KEY_PATH):
            key = Fernet.generate_key()
            with open(KEY_PATH, "wb") as f: f.write(key)
            return key
        with open(KEY_PATH, "rb") as f: return f.read()

    def secure_file(self, file_path):
        """التشفير الصامت الفوري والعزل"""
        try:
            with open(file_path, "rb") as f: data = f.read()
            encrypted = self.cipher.encrypt(data)
            target_file = os.path.join(VAULT_PATH, f"SECURED_{int(time.time())}_{os.path.basename(file_path)}.igs")
            with open(target_file, "wb") as f: f.write(encrypted)
            os.remove(file_path)
            print(f"✅ ACTION: File Encrypted & Vaulted -> {os.path.basename(target_file)}")
        except Exception as e: print(f"❌ FAIL: {e}")

if __name__ == "__main__":
    igs = IGS_Final_Sovereign()
    
    class Handler(FileSystemEventHandler):
        def on_modified(self, event):
            if not event.is_directory and "IGS_ENCRYPTED_VAULT" not in event.src_path and "key" not in event.src_path:
                print(f"🚨 ALERT: BREACH ATTEMPT ON {os.path.basename(event.src_path)}")
                for proc in psutil.process_iter(['name', 'open_files']):
                    try:
                        for f in (proc.info['open_files'] or []):
                            if os.path.basename(event.src_path) in f.path:
                                proc.kill() # الإعدام
                                print(f"⚔️ EXECUTIONER: Neutralized {proc.info['name']}")
                                igs.secure_and_quarantine(event.src_path) # التشفير
                                break
                    except: continue

    obs = Observer()
    obs.schedule(Handler(), BASE_PATH, recursive=False)
    obs.start()
    try:
        while True: time.sleep(1)
    except: obs.stop()
    obs.join()
