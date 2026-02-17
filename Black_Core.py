import os, sys, time, ctypes, threading

class IGSBlack:
    def __init__(self):
        self.cipher_key = "BLACK_INFINITY_2026"
        self.is_cloaked = True

    def memory_scramble(self):
        # محاكاة حماية الذاكرة العشوائية من الرصد
        print("--- [IGS-BLACK] MEMORY CLOAKING ACTIVE ---")
        while self.is_cloaked:
            # هنا يتم "تضليل" عمليات الرصد (Anti-Monitoring)
            time.sleep(5)

    def silent_execution(self):
        # [IGS-BLACK] العمل في صمت مطلق
        print("[+] Absorbing System Traces...")
        # إخفاء النافذة برمجياً فور البدء
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        
    def run(self):
        self.silent_execution()
        threading.Thread(target=self.memory_scramble, daemon=True).start()
        # المحرك يعمل الآن في "البُعد الأسود"
        while True:
            with open(r'D:\IGS_GLOBAL_SYSTEMS\Data_Vault\void.igs', 'a') as f:
                f.write(f"{time.time()}: VOID_STABLE\n")
            time.sleep(60)

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin():
        IGSBlack().run()
