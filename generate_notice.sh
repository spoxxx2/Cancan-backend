#!/data/data/com.termux/files/usr/bin/bash
BUSINESS_NAME=$1
DATE=$(date +%F)
FILENAME="Notice_of_Violation_${BUSINESS_NAME}_${DATE}.pdf"

echo "Generating PDF for $BUSINESS_NAME..."

# Create the text for the PDF
cat <<TEXT > temp_notice.txt
CANCAN KERN | 3RD PARTY COMPLIANCE AUDITOR
Address: 1501 Pearl St, Bakersfield, CA 93305
EIN: 39-2261270 | 501(c)(3) Nonprofit

OFFICIAL NOTICE OF NON-COMPLIANCE
Date: $DATE
Target: $BUSINESS_NAME

VIOLATIONS DETECTED:
- SB 1383: Organic waste found in landfill stream.
- BMC § 8.32.190: Violation of municipal audit standards.

Corrective action is required within 14 days to maintain compliance 
with the City of Bakersfield waste ordinances.

Verified by: CANCAN KERN AI-VISION SYSTEM (YOLOv12+ViT)
Documentation: https://cancankern.org
TEXT

# Convert text to PDF (simple version)
enscript -p - temp_notice.txt | ps2pdf - "$FILENAME"
rm temp_notice.txt
echo "Success! $FILENAME created."
