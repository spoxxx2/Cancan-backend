from fpdf import FPDF
import datetime

class CancanAuditReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'CANCAN: THIRD-PARTY COMPLIANCE AUDIT REPORT', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 5, 'Authorized Compliance Consultant - City of Bakersfield', 0, 1, 'C')
        self.cell(0, 5, '4408 Vern St, Bakersfield, CA', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()} | Authority: BMC § 8.32.190 | Confidential Audit', 0, 0, 'C')

def generate_report(client_name, location, material_data):
    pdf = CancanAuditReport()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 10, f'Audit Date: {datetime.date.today()}', 0, 1)
    pdf.cell(0, 10, f'Client: {client_name}', 0, 1)
    pdf.cell(0, 10, f'Location: {location}', 0, 1)
    pdf.ln(5)
    
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(60, 10, 'Material', 1)
    pdf.cell(40, 10, 'Weight (lbs)', 1)
    pdf.cell(40, 10, 'Condition', 1)
    pdf.cell(50, 10, 'Disposal', 1)
    pdf.ln()

    pdf.set_font('Arial', '', 10)
    for item in material_data:
        pdf.cell(60, 10, item['material'], 1)
        pdf.cell(40, 10, str(item['weight']), 1)
        pdf.cell(40, 10, item['condition'], 1)
        pdf.cell(50, 10, item['disposal'], 1)
        pdf.ln()

    output_file = f"Audit_{client_name.replace(' ', '_')}.pdf"
    pdf.output(output_file)
    print(f"SUCCESS: {output_file} generated.")

materials = [
    {'material': 'PET #1 Plastic', 'weight': 45.2, 'condition': 'Clean', 'disposal': 'Circular Economy'},
    {'material': 'Organic Waste', 'weight': 28.0, 'condition': 'Soiled', 'disposal': 'Compost'}
]

generate_report("Bakersfield Logistics Center", "4408 Vern St", materials)
