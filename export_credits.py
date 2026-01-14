import json
import csv

def export_for_market(json_log):
    with open(json_log, 'r') as f:
        data = json.load(f)
    
    with open('carbon_credits_2026.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Site", "Brand", "Material", "tCO2e_Offset", "Status"])
        for entry in data['data']:
            writer.writerow([
                "2026-01-14", "Bakersfield", entry['brand'], 
                entry['hierarchy'], "0.85", "Unsold"
            ])
    print("Export Complete: carbon_credits_2026.csv is ready for the registry.")

# Run this after your batch scan
