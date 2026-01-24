import requests
import os

url = "http://localhost:8000/batch-scan"
legacy_dir = "./legacy_scans"

files = [('files', open(os.path.join(legacy_dir, f), 'rb')) 
         for f in os.listdir(legacy_dir) if f.endswith(('.jpg', '.png'))]

if files:
    print(f"[SYSTEM] Migrating {len(files)} legacy photos to Pilot Program 2...")
    response = requests.post(url, files=files, data={'humidity': '89'})
    print(f"[SUCCESS] Total Legacy Credits: {response.json()['total_credits']}")
else:
    print("[ERROR] No legacy photos found in ./legacy_scans")
