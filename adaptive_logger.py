import os
import sys
import random
from datetime import datetime

sys.path.append(os.path.expanduser("~/.local/lib/python3.9/site-packages"))
from supabase import create_client

SUPABASE_URL = "https://dzrnwzvizztfmjgvpajd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6cm53enZpenp0Zm1qZ3ZwYWpkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NzM3NDY3OSwiZXhwIjoyMDgyOTUwNjc5fQ.iWYiUTfKpVnLHEkbhIyvo0fzGxNMMpuRn8UIQZp2u5I"

def log_debris_event(metadata):
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Adding Advanced Digital Twin Metadata
        metadata["estimated_value"] = round(random.uniform(0.05, 1.50), 2)  # Simulated USD value
        metadata["contamination_risk"] = "High" if metadata["objects"]["condition"] == "Soiled" else "Low"
        metadata["forecast_50yr"] = {
            "appearance": "Micro-plastic fragmentation / Semi-integrated soil matrix",
            "hazard_level": "Toxic Leachate Potential",
            "recovery_urgency": "Immediate for Circularity"
        }
        
        response = supabase.table("debris_logs").insert(metadata).execute()
        print(f"✅ DIGITAL TWIN LOGGED: {metadata['event_id']}")
        return response
    except Exception as e:
        print(f"❌ Sync Failed: {e}")

if __name__ == "__main__":
    test_data = {
        "event_id": f"NODE-{random.randint(1000,9999)}",
        "objects": {
            "material": "Polymer",
            "sub_type": "PET #1",
            "condition": "Soiled",
            "disposal": "Circular Economy"
        }
    }
    log_debris_event(test_data)
