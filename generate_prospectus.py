import os, sys, json
from datetime import datetime

sys.path.append(os.path.expanduser("~/.local/lib/python3.9/site-packages"))
from supabase import create_client

SUPABASE_URL = "https://dzrnwzvizztfmjgvpajd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6cm53enZpenp0Zm1qZ3ZwYWpkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NzM3NDY3OSwiZXhwIjoyMDgyOTUwNjc5fQ.iWYiUTfKpVnLHEkbhIyvo0fzGxNMMpuRn8UIQZp2u5I"

def generate_report():
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        # Fetch last 5 high-value entries
        data = supabase.table("debris_logs").select("*").limit(5).execute()
        
        print("\n" + "="*50)
        print("  CANCANKERN METADATA PROSPECTUS (SAMPLE)")
        print("  GENERATED: " + datetime.now().strftime("%Y-%m-%d %H:%M"))
        print("="*50 + "\n")
        
        for entry in data.data:
            obj = entry['objects']
            mkt = entry.get('market_data', {})
            print(f"ID: {entry['event_id']}")
            print(f"MATERIAL: {obj['material']} ({obj['sub_type']})")
            print(f"PURITY: {mkt.get('purity_score', 'N/A')}% | MOISTURE: {mkt.get('moisture_content', 'N/A')}")
            print(f"50-YR RISK: {entry.get('forecast_50yr', {}).get('danger_level', 'N/A')}")
            print("-" * 30)
            
        print("\nCONFIDENTIAL: Licensed under Non-Resale Provision.")
        print("Contact data-sales@cancankern.org for full API access.")
        
    except Exception as e:
        print(f"❌ Prospectus Error: {e}")

if __name__ == "__main__":
    generate_report()
