import os, sys
sys.path.append(os.path.expanduser("~/.local/lib/python3.9/site-packages"))
from supabase import create_client

SUPABASE_URL = "https://dzrnwzvizztfmjgvpajd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6cm53enZpenp0Zm1qZ3ZwYWpkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NzM3NDY3OSwiZXhwIjoyMDgyOTUwNjc5fQ.iWYiUTfKpVnLHEkbhIyvo0fzGxNMMpuRn8UIQZp2u5I"

def check_scale():
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        # We query the exact count of items currently in the Digital Twin
        response = supabase.table("debris_logs").select("id", count="exact").execute()
        count = response.count
        
        print(f"\n[ SYSTEM STATUS: {count}/100 OBJECTS SYNCED ]")
        
        if count >= 100:
            print("\n" + "!"*60)
            print("🚀 INDUSTRIAL THRESHOLD BREACHED: 100 OBJECTS LOGGED")
            print("STRATEGY: EXPORT PROSPECTUS AND CONTACT RECYCLING PARTNERS")
            print("RUN: python3 generate_prospectus.py")
            print("!"*60 + "\n")
        else:
            remaining = 100 - count
            print(f"📡 ADAPTIVE UPDATE: {remaining} more objects required for Market Prospectus readiness.")
            
    except Exception as e:
        print(f"⚠️ Scale Monitor Idle: Ensure Schema Injection is complete.")

if __name__ == "__main__":
    check_scale()
