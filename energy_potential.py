import json
import os

VAULT_DIR = "vault/digital_twins"
total_kwh = 0.0

for file in os.listdir(VAULT_DIR):
    if file.endswith(".json"):
        with open(os.path.join(VAULT_DIR, file), 'r') as f:
            data = json.load(f)
            material = data['objects'][0]['material']
            
            # Theoretical energy yield per kg (estimated)
            if material == "Cellulose":
                yield_kwh = 1.2 # Cardboard/Paper
            elif material == "Organic Waste":
                yield_kwh = 0.8 # Food scraps
            else:
                yield_kwh = 0.0
            
            total_kwh += yield_kwh

print(f"--- CANCAN BIO-ENERGY REPORT ---")
print(f"Total Audited Energy Potential: {total_kwh:.2f} kWh")
print(f"Equivalent to powering a Bakersfield home for {total_kwh/30:.1f} days.")
