import os, sys, time, psutil, threading

class IGSNeuronSupreme:
    def __init__(self):
        self.version = "IGS-NEURON-2.0-SUPREME"
        self.safety_status = "STABLE"
        
    def proactive_scan(self):
        # [IGS-NEURON] مراقبة ذكية للتهديدات والموارد
        while True:
            cpu_load = psutil.cpu_percent()
            if cpu_load > 90:
                self.safety_status = "CRITICAL-LOAD"
                # إجراء وقائي: تقليل أولوية العمليات غير الضرورية
            time.sleep(10)

    def display_ui(self):
        os.system('cls')
        print("==========================================")
        print("       INFINITY GLOBAL SYSTEMS (IGS)      ")
        print("      NEURON SUPREME INTERFACE - V2.0     ")
        print("==========================================")
        print(f"CORE STATUS: {self.safety_status}")
        print(f"NEURAL VERSION: {self.version}")
        print("------------------------------------------")
        print("[1] ACTIVATE IGS-SHIELD (Firewall+) ")
        print("[2] DEPLOY IGS-ORACLE (Data Predictor)")
        print("[3] OPEN IGS-VAULT (Secure Access)")
        print("[4] TRIGGER IGS-PURGE (Clean Cache)")
        print("[5] RETREAT (Ghost Mode)")
        print("------------------------------------------")

    def run(self):
        threading.Thread(target=self.proactive_scan, daemon=True).start()
        while True:
            self.display_ui()
            cmd = input("Command -> ")
            if cmd == "5": break
            print(f"Neuron Processing Protocol {cmd}...")
            time.sleep(1)

if __name__ == "__main__":
    IGSNeuronSupreme().run()
