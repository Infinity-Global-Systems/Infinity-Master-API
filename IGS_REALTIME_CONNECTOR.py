
# -*- coding: utf-8 -*-
import requests
import os
import json
from datetime import datetime

# --- ??????? IGS ???????? ---
BASE_PATH = r"E:\IGS_CYBER_PRIME"
LOG_PATH = os.path.join(BASE_PATH, "Threat_Logs")

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

def run_sync():
    print(f"\n>>> [IGS SYSTEM] LIVE SYNC STARTED: {datetime.now().strftime('%H:%M:%S')}")
    # ???? ?????????? ???? ????? ?????????
    url = "https://cve.circl.lu/api/last"
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            data = response.json()[:10]
            
            # ??? ?????? ????? ???????
            file_name = f"Threats_{datetime.now().strftime('%Y%m%d')}.json"
            with open(os.path.join(LOG_PATH, file_name), "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            
            print(f"[SUCCESS] Threat Data Anchored at: {LOG_PATH}\n")
            print("="*60)
            print(f"{'CVE ID':<20} | {'VULNERABILITY SUMMARY'}")
            print("="*60)

            for item in data:
                # ?????? ????? ?????? ????? ?? ??? (id ?? cve) ????? ??? ???? N/A
                cve_id = item.get('id') or item.get('cve') or "VULN-ID-NEW"
                summary = item.get('summary') or item.get('description') or "Detailed analysis pending..."
                
                # ??? ???????? ???? ???? ????
                print(f"{cve_id:<20} | {summary[:80]}...")
            
            print("="*60)
        else:
            print(f"[!] Server Error: {response.status_code}")
    except Exception as e:
        print(f"[CRITICAL] Connection Lost: {e}")

if __name__ == "__main__":
    run_sync()
