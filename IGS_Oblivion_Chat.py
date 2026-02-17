# IGS OBLIVION CHAT V11.0
# [ENCRYPTED-COMMAND-RECEIVER]
# Auth: Infinity (Ya Abqari) - IGS Global

import os
import time
import hashlib

def check_for_commands():
    # هذا المجلد سيعمل كصندوق بريد وهمي داخل الفلاشة
    mailbox = "D:/IGS_GLOBAL_SYSTEMS/01_COMMAND_CENTER/Mailbox"
    if not os.path.exists(mailbox):
        os.makedirs(mailbox)

    print("="*60)
    print("   IGS OBLIVION CHAT - [LISTENING FOR SOVEREIGN SIGNALS]")
    print("="*60)
    print(f"[STATUS] Waiting for Handy-to-ASUS Signal...")

    while True:
        signals = os.listdir(mailbox)
        if signals:
            for signal in signals:
                print(f"\n[!] NEW SIGNAL DETECTED: {signal}")
                # معالجة الإشارة (هنا نضع منطق تنفيذ الأوامر)
                if "SOS" in signal:
                    print("[ACTION] EMERGENCY LOCKDOWN INITIATED!")
                
                # تنظيف الصندوق بعد الاستلام
                os.remove(os.path.join(mailbox, signal))
        
        time.sleep(5) # فحص كل 5 ثوانٍ بصمت

if __name__ == "__main__":
    # تأكد من أن المفاعل يعمل في الخلفية
    try:
        check_for_commands()
    except KeyboardInterrupt:
        print("\n[!] Oblivion Channel Closed.")