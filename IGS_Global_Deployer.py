
# IGS GLOBAL DEPLOYER V1.0
# CONNECTING ASUS SOVEREIGN TO GITHUB CLOUD
# OWNER: INFINITY (YA ABQARI) | igstech@hotmail.com

import os
import subprocess

def deploy_to_infinity_cloud():
    print("="*60)
    print(" IGS GLOBAL SYSTEMS - DEPLOYMENT MODE ACTIVE")
    print("="*60)

    # 1. إعداد هويتك البرمجية (بناءً على طلبك)
    os.system('git config --global user.email "igstech@hotmail.com"')
    os.system('git config --global user.name "Infinity-Global-Systems"')

    # 2. تجهيز المستودع (Repository)
    print("[*] Initializing Sovereign Repository...")
    if not os.path.exists(".git"):
        os.system('git init')

    # 3. إضافة الملفات (المنتج النهائي)
    os.system('git add .')
    
    # 4. رسالة الرفع (Commit)
    commit_msg = "FINAL-REVEAL-OMNIPOTENCE-X1-PRODUCTION-READY"
    os.system(f'git commit -m "{commit_msg}"')

    print("\n[SUCCESS] Files staged and committed.")
    print("[INSTRUCTION] Now link your GitHub URL using: git remote add origin <URL>")
    print("[INSTRUCTION] Then push using: git push -u origin master")

if __name__ == "__main__":
    deploy_to_infinity_cloud()
