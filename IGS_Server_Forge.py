# IGS SERVER FORGE V7.0 - [PLATFORM ORCHESTRATOR]
# Developed for: Infinity (Ya Abqari)
# Target: ASUS Sovereign Server & Global Platforms

import socket
import os
import time

class IGSServer:
    def __init__(self, host='0.0.0.0', port=5555):
        self.host = host
        self.port = port
        self.server_name = "IGS-SOVEREIGN-FORGE"

    def start_platform(self):
        print("="*60)
        print(f"   {self.server_name} - INITIALIZING SERVER FORGE")
        print("="*60)
        
        # إنشاء المقبس (Socket) للربط المباشر
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.host, self.port))
                s.listen()
                ip = socket.gethostbyname(socket.gethostname())
                print(f"[*] Server Forge ACTIVE on IP: {ip} | Port: {self.port}")
                print(f"[*] Waiting for Handy (Mobile) to Link to the Platform...")
                print(f"[*] Logs being sent to: infinitywork30000@gmail.com")
                
                # المفاعل يعمل الآن بشكل تلقائي في الخلفية
                while True:
                    conn, addr = s.accept()
                    with conn:
                        print(f"[!] HANDY CONNECTED: {addr}")
                        conn.sendall(b"IGS PLATFORM ACCESS GRANTED")
                        break
        except Exception as e:
            print(f"[ERROR] Forge Interrupted: {e}")

if __name__ == "__main__":
    forge = IGSServer()
    forge.start_platform()