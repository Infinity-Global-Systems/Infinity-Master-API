from cryptography.fernet import Fernet
import os

class IGS_Vault:
    def __init__(self):
        self.key_path = "D:\\IGS_GLOBAL_SYSTEMS\\04_DATA_ASSETS\\master.key"

    def generate_key(self):
        # إنشاء مفتاح سيادي لأول مرة فقط
        if not os.path.exists(self.key_path):
            key = Fernet.generate_key()
            with open(self.key_path, "wb") as key_file:
                key_file.write(key)
            print("[+] MASTER KEY GENERATED AND SECURED.")

    def encrypt_file(self, file_path):
        with open(self.key_path, "rb") as f:
            key = f.read()
        fernet = Fernet(key)
        with open(file_path, "rb") as f:
            data = f.read()
        encrypted = fernet.encrypt(data)
        with open(file_path, "wb") as f:
            f.write(encrypted)
        print(f"[!] {os.path.basename(file_path)} HAS BEEN ENCRYPTED.")

    def decrypt_file(self, file_path):
        with open(self.key_path, "rb") as f:
            key = f.read()
        fernet = Fernet(key)
        with open(file_path, "rb") as f:
            data = f.read()
        decrypted = fernet.decrypt(data)
        with open(file_path, "wb") as f:
            f.write(decrypted)
        print(f"[#] {os.path.basename(file_path)} HAS BEEN DECRYPTED.")

# تفعيل النظام
if __name__ == "__main__":
    vault = IGS_Vault()
    vault.generate_key()
    # مثال: لتشفير ملف في الخزنة
    # vault.encrypt_file("D:\\IGS_GLOBAL_SYSTEMS\\04_DATA_ASSETS\\oracle_reports.igs")