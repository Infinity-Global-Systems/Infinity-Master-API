# IGS HOSTING SOVEREIGNTY V5.0
# Auth: Infinity (Ya Abqari)
# Role: Turning ASUS into a Sovereign Global Server

import os
import http.server
import socketserver
import time

def start_sovereign_hosting():
    PORT = 8080 # البوابة السيادية
    DIRECTORY = "D:/IGS_GLOBAL_SYSTEMS"
    
    os.chdir(DIRECTORY)
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    print("="*60)
    print("   IGS HOSTING SOVEREIGNTY - THE GLOBAL SERVER IS LIVE")
    print("="*60)
    print(f"[+] HOST: ASUS_SOVEREIGN")
    print(f"[+] ROOT: {DIRECTORY}")
    print(f"[+] PORT: {PORT}")
    print(f"[+] STATUS: Global Access Enabled for Handy (Infinity Only)")
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\n[!] MAPPING COMPLETE: Your Handy can now access the Ractor.")
        print("[*] Monitoring all incoming sovereign requests...")
        httpd.serve_forever()

if __name__ == "__main__":
    start_sovereign_hosting()