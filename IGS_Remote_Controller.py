# IGS REMOTE CONTROLLER V1.5 - [SERVER MODE]
# Designed for: ASUS Sovereign <-> Handy Integration
# Auth: Infinity (Ya Abqari)

import socket
import os
import subprocess

def start_remote_server():
    # إعداد السيرفر لاستقبال أوامر الهاتف
    host = '0.0.0.0' # الاستماع لكافة الأجهزة المرتبطة
    port = 9999      # المنفذ الخاص بـ IGS
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    
    print("="*60)
    print("   IGS REMOTE CONTROL - ASUS CORE IS WAITING")
    print("="*60)
    print(f"[*] Server Listening on Port: {port}")
    print(f"[*] Status: Connected to Drive D:/")
    print("[*] Target: Listening for Infinity's Handy signals...")

    while True:
        client, addr = server.accept()
        print(f"[!] Handy Connected from: {addr}")
        data = client.recv(1024).decode('utf-8')
        
        if data == "OPEN_VAULT":
            os.startfile("D:/IGS_GLOBAL_SYSTEMS/01_COMMAND_CENTER")
            client.send(b"SUCCESS: Vault Opened on ASUS.")
        elif data == "STATUS":
            client.send(b"SUCCESS: IGS Core is 100% Operational.")
        
        client.close()

if __name__ == "__main__":
    start_remote_server()