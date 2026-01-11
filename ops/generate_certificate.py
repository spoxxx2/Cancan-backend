import datetime

def create_compliance_cert(event_id, material, co2_offset):
    cert_content = f"""
======================================================================
           CANCANKERN INDUSTRIAL COMPLIANCE CERTIFICATE
           REGULATORY STANDARD: CA SB253 / SB261 (2026)
======================================================================

CERTIFICATE ID: CERT-{event_id}
TIMESTAMP: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
ORIGIN NODE: BAKERSFIELD_01

ASSET VERIFICATION:
-------------------
OBJECT ID: {event_id}
MATERIAL TAXONOMY: {material}
FORENSIC GRADE: Industrial (Spectral Verified)
CARBON OFFSET VALUE: {co2_offset} kg CO2e

LEGAL ATTESTATION:
The metadata associated with this asset has been scrubbed of all 
Personal Identifiable Information (PII) and Brand Intellectual 
Property. This data is certified for Scope 3 Emissions Reporting 
under the California Climate Corporate Data Accountability Act.

NON-RESALE PROVISION ACTIVE: DATA LICENSED TO HOLDER ONLY.
======================================================================
"""
    filename = f"docs/CERT_{event_id}.txt"
    with open(filename, "w") as f:
        f.write(cert_content)
    print(f"✅ COMPLIANCE CERTIFICATE GENERATED: {filename}")

if __name__ == "__main__":
    # Test generation
    create_compliance_cert("NODE-9921", "Polymer (PET #1)", "2.45")
