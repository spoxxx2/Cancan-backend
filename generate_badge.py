import json
import os

VAULT_DIR = "vault/digital_twins"
total_value = 0.0

# Calculate current value
for file in os.listdir(VAULT_DIR):
    if file.endswith(".json"):
        with open(os.path.join(VAULT_DIR, file), 'r') as f:
            data = json.load(f)
            total_value += data['forecast_2076']['estimated_worth']

# Create a public API-like JSON file
badge_data = {
    "organization": "Cancan",
    "status": "Authorized Auditor (BMC § 8.32.190)",
    "total_methane_credits": f"${total_value:.2f}",
    "last_update": "$(date)"
}

with open("compliance_badge.json", "w") as f:
    json.dump(badge_data, f, indent=4)

print("Compliance Badge API generated.")
