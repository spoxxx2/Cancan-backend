import json
import os
import random

VAULT_DIR = "vault/digital_twins"

for file in os.listdir(VAULT_DIR):
    if file.endswith(".json"):
        with open(os.path.join(VAULT_DIR, file), 'r+') as f:
            data = json.load(f)
            
            # Add Thermal Metadata
            # Simulate a 5-8°C delta for organic decomposition
            temp_delta = random.uniform(2.0, 8.5) 
            
            data["thermal_signature"] = {
                "core_temp_celsius": 22.5 + temp_delta,
                "ambient_temp_celsius": 22.5,
                "methane_leakage_detected": True if temp_delta > 5 else False,
                "spectral_fingerprint": "HS-IR-8842-BAK"
            }
            
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

print("Thermal Methane Interception Layer Hardwired to Vault.")
