# IGS MASTER CONTROLLER V1.0 - [Sovereign Edition]
# Target: ASUS Laptop & Drive D:
# Auth: Infinity (Ya Abqari)

import os

class IGSRactor:
    def __init__(self):
        self.host = "ASUS_SOVEREIGN"
        self.storage = "D:/"
        self.status = "TOTAL-SYNCHRONIZATION"
        self.emails = ["infinitywork30000@gmail.com", "infinitywork3000@hotmail.com", "abdodoc1@hotmail.com"]

    def engage_core(self):
        print(f"[*] Initializing IGS Core on {self.host}...")
        print(f"[*] Locking Persistent Data to {self.storage}...")
        return "IGNITION SUCCESSFUL"

# FEED THE SYSTEM
igs_core = IGSRactor()
igs_core.engage_core()