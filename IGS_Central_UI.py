# IGS-ACTIVATION-CMD: START_SOVEREIGN_SYSTEM
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.filedialog as fd
import os, psutil
from cryptography.fernet import Fernet

class IGSCentralUI:
    def __init__(self, root):
        self.root = root
        self.root.title("INFINITY GLOBAL SYSTEMS - CENTRAL COMMAND v2.0")
        self.root.geometry("1000x650")
        self.root.configure(bg="#050505") # Deep Space Black
        
        # التأكد من وجود مفتاح السيادة (D:)
        if not os.path.exists("D:"):
            messagebox.showerror("CRITICAL ERROR", "IGS-KEY (D:) NOT FOUND. ACCESS DENIED.")
            root.destroy()
            return

        self.setup_ui()
        self.update_pulse()

    def setup_ui(self):
        # Header - الهوية المؤسسية
        header_frame = tk.Frame(self.root, bg="#050505")
        header_frame.pack(pady=20, fill="x")
        
        tk.Label(header_frame, text="INFINITY GLOBAL SYSTEMS", font=("Courier", 28, "bold"), fg="#00ff00", bg="#050505").pack()
        tk.Label(header_frame, text="[ SOVEREIGN PRODUCTION UNIT ]", font=("Courier", 12), fg="#008800", bg="#050505").pack()

        # Main Container
        main_frame = tk.Frame(self.root, bg="#050505")
        main_frame.pack(fill="both", expand=True, padx=30)

        # --- Section 1: System Pulse (النبض الحي) ---
        pulse_frame = tk.LabelFrame(main_frame, text=" SYSTEM PULSE ", fg="#00ff00", bg="#050505", font=("Courier", 12, "bold"))
        pulse_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.cpu_label = tk.Label(pulse_frame, text="CPU USAGE: 0%", fg="#00ff00", bg="#050505", font=("Courier", 14))
        self.cpu_label.pack(pady=20, padx=20)
        
        self.key_status = tk.Label(pulse_frame, text="KEY D: SECURED", fg="#00ff00", bg="#050505", font=("Courier", 10))
        self.key_status.pack(pady=5)

        # --- Section 2: Enterprise Departments (الأقسام التشغيلية) ---
        dept_frame = tk.LabelFrame(main_frame, text=" ENTERPRISE DEPARTMENTS ", fg="#00ff00", bg="#050505", font=("Courier", 12, "bold"))
        dept_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        depts = [
            ("PRODUCTION LINE", "02_PRODUCTION_LINE"),
            ("CYBER SHIELD", "03_CYBER_SHIELD"),
            ("DATA ASSETS", "04_DATA_ASSETS"),
            ("DISTRIBUTION", "05_DISTRIBUTION")
        ]

        for text, folder in depts:
            btn = tk.Button(dept_frame, text=f"GO TO {text}", width=30, bg="#111111", fg="#00ff00", 
                            font=("Courier", 10), activebackground="#00ff00", command=lambda f=folder: self.open_folder(f))
            btn.pack(pady=8, padx=20)

        # --- Section 3: IGS VAULT - AES-256 (الخزنة السيادية) ---
        vault_frame = tk.LabelFrame(main_frame, text=" IGS SOVEREIGN VAULT (AES-256) ", fg="#ff0000", bg="#050505", font=("Courier", 12, "bold"))
        vault_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=20, sticky="nsew")

        tk.Label(vault_frame, text="Manage asset encryption and master keys:", fg="#888888", bg="#050505", font=("Courier", 9)).pack(pady=5)
        
        btn_layout = tk.Frame(vault_frame, bg="#050505")
        btn_layout.pack(pady=10)

        tk.Button(btn_layout, text="LOCK ASSET", bg="#330000", fg="white", width=20, font=("Courier", 10, "bold"),
                  command=lambda: self.toggle_vault("LOCK")).pack(side="left", padx=20)
        
        tk.Button(btn_layout, text="UNLOCK ASSET", bg="#003300", fg="white", width=20, font=("Courier", 10, "bold"),
                  command=lambda: self.toggle_vault("UNLOCK")).pack(side="left", padx=20)

    # --- محرك التشفير المدمج ---
    def toggle_vault(self, action):
        key_dir = "D:\\IGS_GLOBAL_SYSTEMS\\04_DATA_ASSETS"
        key_path = os.path.join(key_dir, "master.key")
        
        if not os.path.exists(key_dir): os.makedirs(key_dir)
        
        # إنشاء مفتاح إذا لم يوجد
        if not os.path.exists(key_path):
            key = Fernet.generate_key()
            with open(key_path, "wb") as kf: kf.write(key)
            messagebox.showinfo("VAULT", "NEW MASTER KEY GENERATED IN 04_DATA_ASSETS.")
        
        with open(key_path, "rb") as kf: key = kf.read()
        fnt = Fernet(key)
        
        target = fd.askopenfilename(initialdir="D:\\IGS_GLOBAL_SYSTEMS", title=f"Select File to {action}")
        if target:
            try:
                with open(target, "rb") as f: data = f.read()
                if action == "LOCK":
                    processed = fnt.encrypt(data)
                    status = "LOCKED (ENCRYPTED)"
                else:
                    processed = fnt.decrypt(data)
                    status = "UNLOCKED (DECRYPTED)"
                
                with open(target, "wb") as f: f.write(processed)
                messagebox.showinfo("SUCCESS", f"File {status} successfully.")
            except Exception as e:
                messagebox.showerror("VAULT ERROR", f"Security Alert: {str(e)}")

    def open_folder(self, folder):
        path = f"D:\\IGS_GLOBAL_SYSTEMS\\{folder}"
        if os.path.exists(path):
            os.startfile(path)
        else:
            messagebox.showwarning("PATH ERROR", f"Department {folder} not found.")

    def update_pulse(self):
        try:
            cpu = psutil.cpu_percent()
            self.cpu_label.config(text=f"CPU USAGE: {cpu}%")
            if not os.path.exists("D:"):
                self.root.destroy()
            self.root.after(1000, self.update_pulse)
        except:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = IGSCentralUI(root)
    root.mainloop()