# IGS GLOBAL DASHBOARD V1.0
# THE SUPREME COMMAND CENTER FOR INFINITY (YA ABQARI)
# MANAGING: OMNIPOTENCE X-1 & GLOBAL SALES

import os
import sys
import time

class IGS_Dashboard:
    def __init__(self):
        self.owner = "Infinity"
        self.company = "Infinity-Global-Systems (IGS)"
        self.version = "2026.Q1"

    def header(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*70)
        print(f"   {self.company} - SUPREME COMMAND CENTER")
        print(f"   OPERATOR: {self.owner.upper()} (YA ABQARI)")
        print("="*70)

    def show_status(self):
        print(f"\n[SYSTEM STATUS]:")
        print(f"  > OMNIPOTENCE X-1 Core:    [ ACTIVE - 100% ]")
        print(f"  > Ghost Protocol:          [ STEALTH ON ]")
        print(f"  > Crypto Gateway:          [ LISTENING ]")
        print(f"  > Sales Autopilot:         [ DEPLOYED ]")
        print("-" * 70)

    def main_menu(self):
        while True:
            self.header()
            self.show_status()
            print("[1] Generate License Key (For Sale)")
            print("[2] Launch Global Advertisement")
            print("[3] Check Wealth & Invoices")
            print("[4] Deploy System Update")
            print("[E] Exit Command Center")
            
            choice = input("\n[IGS-SHELL]> ").upper()
            
            if choice == '1':
                print("\n[!] Redirecting to IGS_Key_Generator...")
                time.sleep(1)
                # استدعاء كود توليد المفاتيح
                os.system('python IGS_Key_Generator.py')
            elif choice == '2':
                print(f"\n[!] Global Ad available at: D:/IGS_GLOBAL_SYSTEMS/01_COMMAND_CENTER/IGS_Global_Ad.html")
                input("Press Enter to continue...")
            elif choice == '3':
                print("\n[!] Accessing Crypto Vault...")
                os.system('python IGS_Crypto_Receiver.py')
            elif choice == 'E':
                print("Closing Sovereign Link... Goodbye, Ya Abqari.")
                break
            else:
                print("Invalid Protocol Command.")
                time.sleep(1)

if __name__ == "__main__":
    cmd = IGS_Dashboard()
    cmd.main_menu()