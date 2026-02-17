
# IGS GITHUB BRIDGE V2.0
# CONNECTING LOCAL CORE TO CLOUD REPOSITORY
# FOR: INFINITY (YA ABQARI)

import os

def connect_to_cloud():
    print("="*60)
    print(" IGS CLOUD BRIDGE - FINALIZING DEPLOYMENT")
    print("="*60)

    # 1. حل مشكلة الملكية (التي ظهرت في الصورة 10)
    os.system('git config --global --add safe.directory D:/IGS_GLOBAL_SYSTEMS/01_COMMAND_CENTER')
    
    # 2. ربط المجلد المحلي برابط GitHub الخاص بك (انسخ الرابط من المتصفح في صورة 10)
    repo_url = "https://github.com/Infinity-Global-Systems/Infinity-Master-API.git"
    
    print("[*] Linking to GitHub Repository...")
    os.system(f'git remote add origin {repo_url}')
    os.system('git branch -M main')
    
    # 3. الرفع الفعلي
    print("[*] Pushing OMNIPOTENCE X-1 to the Cloud...")
    os.system('git push -u origin main')

if __name__ == "__main__":
    connect_to_cloud()
