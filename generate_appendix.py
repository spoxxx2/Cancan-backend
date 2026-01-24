import os
import json
from fpdf import FPDF

class AuditPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'CANCAN - Digital Twin Audit Appendix (BMC § 8.32.190)', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_report():
    pdf = AuditPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 10)
    
    # Table Header
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(45, 10, 'Event ID', 1, 0, 'C', 1)
    pdf.cell(35, 10, 'Material', 1, 0, 'C', 1)
    pdf.cell(30, 10, 'Condition', 1, 0, 'C', 1)
    pdf.cell(40, 10, 'Worth (2076)', 1, 0, 'C', 1)
    pdf.cell(40, 10, 'Impact Score', 1, 1, 'C', 1)

    vault_dir = "vault/digital_twins"
    for file in sorted(os.listdir(vault_dir)):
        if file.endswith(".json"):
            with open(os.path.join(vault_dir, file), 'r') as f:
                data = json.load(f)
                obj = data['objects'][0]
                
                pdf.cell(45, 10, file.replace('_twin.json', '')[:15], 1)
                pdf.cell(35, 10, obj['material'], 1)
                pdf.cell(30, 10, obj['state'], 1)
                pdf.cell(40, 10, f"${data['forecast_2076']['estimated_worth']:.2f}", 1)
                pdf.cell(40, 10, str(data['environmental_impact_score']), 1, 1)

    pdf.output("Cancan_Audit_Appendix.pdf")
    print("Appendix PDF generated successfully.")

if __name__ == "__main__":
    generate_report()
