
# -*- coding: utf-8 -*-
import os
from cryptography.fernet import Fernet
import customtkinter as ctk
from tkinter import messagebox

# --- إعدادات السيادة ---
BASE_PATH = r"E:\IGS_CYBER_PRIME"
VAULT_PATH = os.path.join(BASE_PATH, "IGS_ENCRYPTED_VAULT")
KEY_PATH = os.path.join(BASE_PATH, "IGS_MASTER.key")

class IGSDecryptor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("IGS MASTER DECRYPTOR - OWNER ONLY")
        self.geometry("600x400")
        ctk.set_appearance_mode("Dark")
        
        # تحميل المفتاح السيادي
        if not os.path.exists(KEY_PATH):
            messagebox.showerror("CRITICAL ERROR", "Master Key Missing! Files cannot be recovered.")
            self.destroy()
            return
            
        with open(KEY_PATH, "rb") as f:
            self.cipher = Fernet(f.read())

        self.setup_ui()

    def setup_ui(self):
        ctk.CTkLabel(self, text="IGS RECOVERY PORTAL", font=("Orbitron", 20, "bold"), text_color="#00D4FF").pack(pady=30)
        
        self.btn_restore = ctk.CTkButton(self, text="RESTORE ALL FILES FROM VAULT", 
                                         fg_color="#1f538d", hover_color="#005fb8",
                                         command=self.restore_files, font=("Consolas", 14, "bold"))
        self.btn_restore.pack(pady=20, padx=50, fill="x")

        self.status_log = ctk.CTkTextbox(self, height=150, font=("Consolas", 12))
        self.status_log.pack(pady=20, padx=20, fill="both")

    def restore_files(self):
        files = [f for f in os.listdir(VAULT_PATH) if f.endswith(".igs")]
        if not files:
            messagebox.showinfo("INFO", "Vault is empty. No files to restore.")
            return

        for f_name in files:
            try:
                enc_path = os.path.join(VAULT_PATH, f_name)
                with open(enc_path, "rb") as f:
                    encrypted_data = f.read()
                
                # فك التشفير
                decrypted_data = self.cipher.decrypt(encrypted_data)
                
                # استعادة الاسم الأصلي (إزالة البادئة SECURED_timestamp_)
                original_name = "_".join(f_name.split("_")[2:]).replace(".igs", "")
                original_path = os.path.join(BASE_PATH, original_name)
                
                with open(original_path, "wb") as f:
                    f.write(decrypted_data)
                
                os.remove(enc_path) # حذف النسخة المشفرة بعد النجاح
                self.status_log.insert("end", f"Successfully Restored: {original_name}\n")
            except Exception as e:
                self.status_log.insert("end", f"Error restoring {f_name}: {str(e)}\n")
        
        messagebox.showinfo("SUCCESS", "All files have been returned to the sovereign zone.")

if __name__ == "__main__":
    app = IGSDecryptor()
    app.mainloop()
