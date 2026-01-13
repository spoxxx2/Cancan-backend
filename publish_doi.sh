#!/bin/bash
echo "📡 PUBLISHING DOI: 10.AUDIT/BAKERSFIELD.2026.01.13"

# Inject DOI into the landing page for transparency
sed -i 's/DOI: .*/DOI: 10.AUDIT\/BAKERSFIELD.2026.01.13/g' index.html

# Copy the raw JSON to the public root for scrapers/researchers
cp audit_record_final.json doi_record.json

# Commit to the permanent Mothership ledger
git add index.html doi_record.json audit_record_final.json
git commit -m "OFFICIAL DOI PUBLICATION: 10.AUDIT/BAKERSFIELD.2026.01.13"
git push origin main
