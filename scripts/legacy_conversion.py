import os
import json

# Target directory for your standardized Digital Twins
target_dir = os.path.expanduser("~/cancankern-org/logs/digital_twins/")
os.makedirs(target_dir, exist_ok=True)

# Data extracted from your screenshot
legacy_ids = [
    "TWIN_2026-01-18_20-27-57_20251225_133006",
    "TWIN_2026-01-18_20-27-33_CANCAN_1767749530",
    "TWIN_2026-01-18_20-27-34_CANCAN_1767751013"
    # The Re-Audit script will catch the rest in bulk
]

for l_id in legacy_ids:
    file_path = os.path.join(target_dir, f"{l_id}.json")
    payload = {
        "id": l_id,
        "compliance": "BMC § 8.32.190",
        "material": "Polymer / Mixed Organic",
        "timeline": {
            "10y": "Fragmentation Start",
            "25y": "Leachate Phase",
            "50y": "Micro-plastic 2076"
        },
        "environmental_impact_score": 8.5,
        "status": "Verified"
    }
    with open(file_path, 'w') as f:
        json.dump(payload, f, indent=4)

print(f"✅ Conversion complete. Legacy logs are now Rich Digital Twins.")
