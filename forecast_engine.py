import json
import os

VAULT_DIR = "vault/digital_twins"

def get_forecast(material, condition, years):
    if "Organic" in material:
        if years == 10: return {"state": "Active Decomposition", "worth": "$12", "danger": "Med (Methane)"}
        if years == 25: return {"state": "Stabilized Humus", "worth": "$30", "danger": "Low"}
        if years == 50: return {"state": "Carbon-Sequested Soil", "worth": "$50", "danger": "Zero"}
    elif "Plastic" in material or "Polymer" in material:
        if years == 10: return {"state": "Integrity Loss", "worth": "$0", "danger": "High"}
        if years == 25: return {"state": "Macro-fragmentation", "worth": "$0", "danger": "Extreme"}
        if years == 50: return {"state": "Micro-plastic Leaching", "worth": "-$100 (Cleanup)", "danger": "Critical"}
    return {"state": "Degrading", "worth": "Unknown", "danger": "Varies"}

def update_vault_forecasts():
    for file in os.listdir(VAULT_DIR):
        if file.endswith(".json"):
            with open(os.path.join(VAULT_DIR, file), 'r+') as f:
                data = json.load(f)
                mat = data['objects'][0]['material']
                cond = data['objects'][0]['condition']
                
                # Hardwiring the multi-generational forecast
                data['forecasts'] = {
                    "2036": get_forecast(mat, cond, 10),
                    "2051": get_forecast(mat, cond, 25),
                    "2076": get_forecast(mat, cond, 50)
                }
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
    print("PHANTOM UPDATE: 10, 25, and 50 Year Timelines Hardwired.")

if __name__ == "__main__":
    update_vault_forecasts()
