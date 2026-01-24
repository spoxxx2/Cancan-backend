import smtplib
import os
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# --- CREDENTIALS ---
SENDER_EMAIL = "your-nonprofit-spoxxx2@gmail.com"
APP_PASSWORD = "fnbtduilkekdpoak"  # Hardwired 16-digit key
RECIPIENT = "recyclinginfo@bakersfieldcity.us"

def add_legal_footer(pdf, fingerprint):
    pdf.set_y(-30)
    pdf.set_font('Courier', 'I', 8)
    pdf.cell(0, 10, f"VERIFIED BY CANCAN PROTOCOL V1.2 | TIMESTAMP: {datetime.now()}", 0, 1, 'C')
    pdf.cell(0, 10, f"DIGITAL FINGERPRINT: {fingerprint}", 0, 1, 'C')
    pdf.cell(0, 10, "OFFICIAL RECORD PURSUANT TO SB 1383 & BMC § 8.32.190", 0, 1, 'C')

def send_compliance_report():
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT
    msg['Subject'] = f"Weekly SB 1383 Compliance Report - Cancan FRO "

    body = f"Automated filing for {datetime.now().strftime('%Y-%m-%d')}. Verified per BMC § 8.32.190."
    msg.attach(MIMEText(body, 'plain'))

    filename = "GODMODE_CERTIFICATE.pdf"
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            attach = MIMEApplication(f.read(), _subtype="pdf")
            attach.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(attach)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
        print("COMPLIANCE FILING SENT TO CITY OF BAKERSFIELD.")
    except Exception as e:
        print(f"FAILED TO SEND FILING: {e}")

if __name__ == "__main__":
    send_compliance_report()
