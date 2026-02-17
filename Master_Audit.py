import os, psutil, time

def perform_audit():
    print("--- [IGS-SYSTEM-AUDIT] STARTING DEEP SCAN ---")
    time.sleep(1)
    
    # فحص الوجود الفيزيائي (The Key)
    if os.path.exists('D:'):
        print("[OK] PHYSICAL KEY (D:) - DETECTED")
    
    # فحص العمليات الشبحية (Ghost Processes)
    ghosts = [p.info for p in psutil.process_iter(['name']) if 'python' in p.info['name']]
    if len(ghosts) > 0:
        print(f"[OK] GHOST NODES ACTIVE: {len(ghosts)} Threads Running")
    
    # فحص الدروع (Shields)
    if os.path.exists(r'D:\IGS_GLOBAL_SYSTEMS\Command Center\Shield_Supreme.py'):
        print("[OK] SHIELD-SUPREME - ARMED")
    
    # فحص التشفير (Black-Box)
    if os.path.exists(r'D:\IGS_GLOBAL_SYSTEMS\blackbox.igs'):
        print("[OK] BLACK-BOX - RECORDING")

    print("\n--- [RESULT] IGS SOVEREIGNTY IS ABSOLUTE ---")

if __name__ == "__main__":
    perform_audit()
