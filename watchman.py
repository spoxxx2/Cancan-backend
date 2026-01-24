import os
import time
import subprocess

WATCH_DIR = "photos"
PROCESSOR = "process_legacy.py" # We will reuse your logic

print(f"Monitoring {WATCH_DIR} for new audit data...")

def get_files():
    return set(os.listdir(WATCH_DIR))

initial_files = get_files()

try:
    while True:
        time.sleep(5)
        current_files = get_files()
        new_files = current_files - initial_files
        
        if new_files:
            for file in new_files:
                if file.endswith(".jpg"):
                    print(f"New Scan Detected: {file}. Hardwiring to vault...")
                    subprocess.run(["python3", PROCESSOR])
            initial_files = current_files
except KeyboardInterrupt:
    print("Watchman standing down.")
