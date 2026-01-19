import os
import json
import csv

log_dir = os.path.expanduser("~/cancankern-org/logs/digital_twins/")
output_file = os.path.expanduser("~/cancankern-org/docs/compliance/MASTER_IMPACT_LEDGER.csv")

def generate():
    files = [f for f in os.listdir(log_dir) if f.endswith('.json')]
    data_rows = []
    total_kg = 0
    
    headers = [
        "Audit_ID", "Timestamp", "Material", "CO2e_kg", 
        "Market_Value_USD", "BSF_Larvae_Yield_kg", "Frass_Yield_kg"
    ]

    for filename in files:
        path = os.path.join(log_dir, filename)
        with open(path, 'r') as f:
            try:
                d = json.load(f)
                kg = d.get("environmental_impact_score", 0.45)
                total_kg += kg
                
                # GOLDEN BOOST MATH
                val = (kg / 1000) * 28.50 # Carbon Market Value
                bsf_larvae = kg * 0.20     # 20% conversion to larvae
                bsf_frass = kg * 0.50      # 50% conversion to fertilizer
                
                row = [
                    d.get("id", filename),
                    d.get("audit_timestamp", "2026-01-18"),
                    d.get("taxonomy", {}).get("material", "Organic"),
                    round(kg, 2),
                    f"${val:.4f}",
                    round(bsf_larvae, 2),
                    round(bsf_frass, 2)
                ]
                data_rows.append(row)
            except:
                continue

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data_rows)

    print(f"--- GOLDEN LEDGER UPDATED ---")
    print(f"Total Diversion: {total_kg:.2f} kg")
    print(f"Total Market Value: ${((total_kg/1000)*28.50):.2f}")
    print(f"Potential BSF Protein: {(total_kg*0.20):.2f} kg")

if __name__ == "__main__":
    generate()
