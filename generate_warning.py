from fpdf import FPDF
import json
import os

def create_warning(audit_file):
    with open(audit_file, 'r') as f:
        data = json.load(f)
    
    # Only generate if contamination is high (logic can be adjusted)
    if data['objects'][0].get('environmental_impact_score', 0) > 5:
        pdf = FPDF()
        pdf.add_page()
        
        # Header - Formal & Strict
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, "OFFICIAL NOTICE OF NON-COMPLIANCE", ln=True, align='C')
        pdf.set_font("Arial", 'B', 10)
        pdf.cell(200, 10, "BAKERSFIELD ORGANIC WASTE RECOVERY INITIATIVE", ln=True, align='C')
        pdf.ln(10)
        
        # Body
        pdf.set_font("Arial", size=11)
        pdf.multi_cell(0, 10, f"On {data['timestamp']}, an automated audit (ID: {data['id']}) was performed at this location. "
                             f"Our sensors identified {data['material']} with a significant contamination risk.")
        pdf.ln(5)
        pdf.set_font("Arial", 'B', 11)
        pdf.multi_cell(0, 10, "LEGAL CITATION: BMC § 8.32.190")
        pdf.set_font("Arial", size=11)
        pdf.multi_cell(0, 10, "Under SB 1383 and local Bakersfield ordinance, businesses must ensure "
                             "proper separation of organic waste to avoid administrative civil penalties.")
        
        # Future Liability
        pdf.ln(5)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, f"PROJECTED 2076 ENVIRONMENTAL LIABILITY: {data['worth_2076']}", ln=True)
        
        # Signature
        pdf.ln(20)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 10, "CANCAN SENTINEL SYSTEM - AUTOMATED COMPLIANCE NODE", ln=True)
        
        pdf.output(f"WARNING_{data['id']}.pdf")
        print(f"WARNING GENERATED: WARNING_{data['id']}.pdf")
    else:
        print("Audit within acceptable limits. No warning required.")

if __name__ == "__main__":
    vault = "vault/digital_twins/"
    latest = max([os.path.join(vault, f) for f in os.listdir(vault) if f.endswith('.json')], key=os.path.getmtime)
    create_warning(latest)
