from fpdf import FPDF
import json
import os

def create_pdf(audit_file):
    with open(audit_file, 'r') as f:
        data = json.load(f)

    pdf = FPDF()
    pdf.add_page()
    
    # Header
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "CANCAN: ENVIRONMENTAL COMPLIANCE REPORT", ln=True, align='C')
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, "Issued Pursuant to BMC § 8.32.190 | SB 1383 Recovery Node", ln=True, align='C')
    pdf.line(10, 30, 200, 30)

    # Audit Metadata
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"Audit ID: {data['detection_event']}", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 8, f"Timestamp: {data['timestamp']}", ln=True)
    pdf.cell(0, 8, f"Spectral Fingerprint: {data['objects'][0]['spectral_fingerprint'][:20]}...", ln=True)

    # Sustainability Metrics
    pdf.ln(5)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, " SUSTAINABILITY DATA", ln=True, fill=True)
    pdf.cell(0, 8, f"Material: {data['objects'][0]['material']}", ln=True)
    pdf.cell(0, 8, f"Impact Score: {data['objects'][0]['environmental_impact_score']}/10", ln=True)

    # 50-Year Forecast
    pdf.ln(5)
    pdf.set_fill_color(230, 245, 230)
    pdf.cell(0, 10, " 2076 DIGITAL TWIN FORECAST", ln=True, fill=True)
    pdf.cell(0, 8, f"State: {data['forecasts']['2076']['state']}", ln=True)
    pdf.cell(0, 8, f"Projected Value: {data['forecasts']['2076']['worth']}", ln=True)

    # Footer/Legal
    pdf.set_y(-30)
    pdf.set_font("Arial", 'I', 8)
    pdf.multi_cell(0, 5, "This document serves as an official record of organic waste diversion. Data verified via YOLOv12 + Hyperspectral Fingerprinting.")

    pdf.output(f"{data['detection_event']}_Report.pdf")
    print(f"REPORT GENERATED: {data['detection_event']}_Report.pdf")

if __name__ == "__main__":
    # Runs on the latest audit in the vault
    vault = "vault/digital_twins/"
    files = [os.path.join(vault, f) for f in os.listdir(vault) if f.endswith('.json')]
    if files:
        latest = max(files, key=os.path.getmtime)
        create_pdf(latest)
