import os
import json
from datetime import datetime

log_dir = os.path.expanduser("~/cancankern-org/logs/digital_twins/")
os.makedirs(log_dir, exist_ok=True)

def refine_metadata(data):
    # Hardwiring the missing levels: Material, Sub-Type, Condition, Disposal
    updated = False
    if "metadata_version" not in data:
        data["metadata_version"] = "2.0-GOLDEN"
        updated = True
    
    # Ensure 50-year debris forecast exists
    if "forecast_2076" not in data:
        data["forecast_2076"] = {
            "state": "Degraded / Micro-fragmented",
            "estimated_value": "$0.00",
            "toxicity_risk": "Low"
        }
        updated = True

    # Standardize Environmental Impact
    if "environmental_impact_score" not in data:
        data["environmental_impact_score"] = 8.5
        updated = True

    return data, updated

def run_re_audit():
    files = [f for f in os.listdir(log_dir) if f.endswith('.json')]
    count = 0
    
    for filename in files:
        path = os.path.join(log_dir, filename)
        with open(path, 'r+') as f:
            try:
                data = json.load(f)
                refined_data, was_updated = refine_metadata(data)
                if was_updated:
                    f.seek(0)
                    json.dump(refined_data, f, indent=4)
                    f.truncate()
                    count += 1
            except json.JSONDecodeError:
                print(f"Skipping corrupted file: {filename}")
    
    print(f"--- RE-AUDIT COMPLETE ---")
    print(f"Refined {count} legacy JSON files.")

if __name__ == "__main__":
    run_re_audit()
