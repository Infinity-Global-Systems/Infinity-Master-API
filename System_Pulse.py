import os, sys, time, psutil, ctypes

def get_drive_status(drive_letter):
    return os.path.exists(f"{drive_letter}:")

class IGSPulse:
    def __init__(self):
        self.node_name = "IGS-ASUS-MASTER"
        
    def monitor(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==========================================")
        print("       INFINITY GLOBAL SYSTEMS (IGS)      ")
        print("          SYSTEM PULSE MONITOR            ")
        print("==========================================")
        
        while True:
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            drive_ok = get_drive_status("D")
            
            # عرض الحالة بأسلوب سيادي
            status = "HEALTHY" if cpu < 80 and drive_ok else "STRESSED"
            if not drive_ok: status = "CRITICAL: KEY REMOVED"
            
            print(f"\r[PULSE] CPU: {cpu}% | RAM: {ram}% | DRIVE D: {'ONLINE' if drive_ok else 'OFFLINE'} | STATUS: {status}", end="")
            
            # تسجيل النبض في الصندوق الأسود (IGS-BLACK-BOX)
            with open(r'D:\IGS_GLOBAL_SYSTEMS\blackbox.igs', 'a') as f:
                f.write(f"{time.time()}|{cpu}|{ram}|{status}\n")
                
            if not drive_ok:
                print("\n[!] EMERGENCY: KEY DISCONNECTED. SHUTTING DOWN CORE.")
                break
            time.sleep(0.5)

if __name__ == "__main__":
    pulse = IGSPulse()
    pulse.monitor()
