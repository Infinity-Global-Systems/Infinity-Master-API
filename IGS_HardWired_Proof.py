# IGS HARD-WIRED PROOF V5.0
# [PHYSICAL-IDENTITY-STAMP]
# Auth: Infinity (Ya Abqari) - IGS Global

import os
import platform
import uuid
import hashlib

def generate_proof():
    print("="*60)
    print("   IGS HARD-WIRED PROOF - [GENERATING SYSTEM DNA]")
    print("="*60)
    
    # استخراج هوية الجهاز المادية (HWID)
    node_id = str(uuid.getnode())
    system_info = platform.uname()
    raw_id = f"{node_id}-{system_info.node}-{system_info.processor}"
    igs_fingerprint = hashlib.sha256(raw_id.encode()).hexdigest().upper()
    
    print(f"[+] DEVICE NAME: {system_info.node}")
    print(f"[+] HARDWARE ID: {node_id}")
    print(f"[+] IGS FINGERPRINT: {igs_fingerprint[:16]}...")
    
    # خلق ملف الإثبات المادي في الفلاشة
    proof_path = "D:/IGS_GLOBAL_SYSTEMS/01_COMMAND_CENTER/IGS_IDENTITY.proof"
    with open(proof_path, "w") as f:
        f.write(f"OFFICIAL IGS SOVEREIGN DEVICE\n")
        f.write(f"OWNER: INFINITY (YA ABQARI)\n")
        f.write(f"DNA: {igs_fingerprint}\n")
        f.write(f"AUTHORIZED EMAILS: infinitywork30000@gmail.com, abdodoc1@hotmail.com\n")
    
    print(f"\n[SUCCESS] Hard-Wired Proof established on Drive D.")
    print(f"[STATUS] This ASUS Laptop is now a Certified IGS Node.")

if __name__ == "__main__":
    generate_proof()