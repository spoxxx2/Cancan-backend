import json
import os

VAULT_DIR = "vault/digital_twins"
total_nitrogen = 0.0 # kg
total_acres_impact = 0.0

for file in os.listdir(VAULT_DIR):
    if file.endswith(".json"):
        with open(os.path.join(VAULT_DIR, file), 'r') as f:
            data = json.load(f)
            # Standard estimates for organic waste NPK content
            if data['objects'][0]['material'] == "Cellulose":
                total_nitrogen += 0.05 
            elif data['objects'][0]['material'] == "Organic Waste":
                total_nitrogen += 0.15 

# 1 acre of depleted soil needs ~50kg of N for restoration
total_acres_impact = total_nitrogen / 50.0

print(f"--- CANCAN MOLECULAR PROVENANCE ---")
print(f"Total Nitrogen Recovered: {total_nitrogen:.2f} kg")
print(f"Bakersfield Soil Regeneration Potential: {total_acres_impact:.4f} Acres")
