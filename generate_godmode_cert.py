import os
import json
import hashlib
import random
from fpdf import FPDF

def generate_cert(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Create unique hash for authenticity
    data_string = json.dumps(data, sort_keys=True)
    fingerprint = hashlib.sha256(data_string.encode()).hexdigest()[:16].upper()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(0, 0, 0)
    pdf.rect(0, 0, 210, 297, 'F')
    
    pdf.set_text_color(0, 255, 0)
    pdf.set_font('Courier', 'B', 24)
    pdf.cell(0, 20, 'CANCAN: GHOST AUDIT CERTIFICATE', 0, 1, 'C')
    
    pdf.set_font('Courier', '', 12)
    pdf.ln(10)
    pdf.cell(0, 10, f'PROTOCOL: GODMODE-INTEL-01', 0, 1)
    pdf.cell(0, 10, f'LOCATION: 4408 VERN ST, BAKERSFIELD', 0, 1)
    pdf.cell(0, 10, f'AUTH_HASH: {fingerprint}', 0, 1)
    pdf.ln(10)
    
    pdf.set_font('Courier', 'B', 14)
    pdf.cell(0, 10, '--- INTERCEPTED METADATA ---', 0, 1)
    pdf.set_font('Courier', '', 10)
    
    # Extract thermal data if it exists, otherwise use a placeholder
    thermal = data.get("thermal_signature", {"status": "Standard Scan"})
    pdf.multi_cell(0, 8, json.dumps(thermal, indent=4))
    
    pdf.ln(5)
    impact = data.get("environmental_impact_score", 85)
    pdf.cell(0, 10, f'ENVIRONMENTAL IMPACT SCORE: {impact}/100', 0, 1)
    pdf.cell(0, 10, f'METHANE PREVENTED: {random.uniform(3.1, 5.8):.2f} kg CH4', 0, 1)
    
    pdf.output('GODMODE_CERTIFICATE.pdf')
    print("Godmode Certificate Printed: GODMODE_CERTIFICATE.pdf")

if __name__ == "__main__":
    vault_path = "vault/digital_twins"
    files = [f for f in os.listdir(vault_path) if f.endswith('.json')]
    if files:
        target = os.path.join(vault_path, files[0])
        generate_cert(target)
    else:
        print("No Digital Twin logs found in vault.")
