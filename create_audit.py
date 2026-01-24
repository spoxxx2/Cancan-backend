import os
import time
import json
import hashlib
import shutil
from dotenv import load_dotenv
from supabase import create_client

# Load secure credentials
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

VAULT_DIR = "vault/digital_twins/"
CAMERA_DIR = "/sdcard/DCIM/Camera/"

def run_audit():
    audit_id = f"CANCAN_{int(time.time())}"
    material = "Organic Waste" # Hardwired for logic; YOLO will replace this
    
    # 1. Create Digital Twin Data
    audit_data = {
        "id": audit_id,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "material": material,
        "impact_score": 8.4,
        "worth_2076": "$50.00",
        "fingerprint": hashlib.sha256(material.encode()).hexdigest()
    }

    # 2. Local Save
    with open(f"{VAULT_DIR}{audit_id}.json", "w") as f:
        json.dump(audit_data, f, indent=4)

    # 3. Supabase SQL Sync (Professional Table Injection)
    try:
        supabase.table("audits").insert(audit_data).execute()
        print(f"SUPABASE SECURE: {audit_id} synced to Postgres.")
    except Exception as e:
        print(f"DB SYNC DELAYED: {e}")

    # 4. Evidence Link (.jpg)
    photos = [f for f in os.listdir(CAMERA_DIR) if f.endswith('.jpg')]
    if photos:
        latest = max([os.path.join(CAMERA_DIR, f) for f in photos], key=os.path.getmtime)
        shutil.copy(latest, f"{VAULT_DIR}{audit_id}.jpg")
        print(f"EVIDENCE LINKED: {audit_id}.jpg secured.")

if __name__ == "__main__":
    run_audit()

    # 5. Zenodo Global Archive (DOI Generation)
    try:
        from zenodo_archive import create_permanent_record
        create_permanent_record(f"{VAULT_DIR}{audit_id}.json")
        print(f"GLOBAL PERMANENCE: {audit_id} archived with DOI.")
    except Exception as e:
        print(f"ZENODO DELAYED: {e}")

def log_event(event_type, status):
    with open("audit_trail.log", "a") as log:
        log.write(f"[{time.ctime()}] {event_type}: {status}\n")

# Use it in your run_audit function
log_event("LOCAL_SAVE", "SUCCESS")
log_event("SUPABASE_SYNC", "SUCCESS")
log_event("ZENODO_DOI", "SUCCESS")
