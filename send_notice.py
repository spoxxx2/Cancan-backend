import smtplib
import os
import json
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def mail_warning(recipient_email, audit_id):
    msg = EmailMessage()
    msg['Subject'] = f"OFFICIAL NOTICE: SB 1383 Compliance Audit {audit_id}"
    msg['From'] = "CANCAN Enforcement <your-email@gmail.com>"
    msg['To'] = recipient_email

    msg.set_content(f"Please find the attached compliance report for the audit conducted on {audit_id}.\n\n"
                    f"This is an automated notification pursuant to BMC § 8.32.190.\n"
                    f"Digital Evidence Link: https://dzrnwzvizztfmjgvpajd.supabase.co")

    # Attach the generated PDF
    pdf_filename = f"WARNING_{audit_id}.pdf"
    if os.path.exists(pdf_filename):
        with open(pdf_filename, 'rb') as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=pdf_filename)

    # SMTP Server Login (Using Environment Variables)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            smtp.send_message(msg)
        print(f"NOTICE SERVED: Email sent to {recipient_email}")
    except Exception as e:
        print(f"MAIL ERROR: {e}")

if __name__ == "__main__":
    # Example usage: Replace with actual logic to pull email from a database
    import sys
    if len(sys.argv) > 2:
        mail_warning(sys.argv[1], sys.argv[2])
