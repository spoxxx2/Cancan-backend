import os, sys
sys.path.append(os.path.expanduser("~/.local/lib/python3.9/site-packages"))
from supabase import create_client

# Credentials
URL = "https://dzrnwzvizztfmjgvpajd.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6cm53enZpenp0Zm1qZ3ZwYWpkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NzM3NDY3OSwiZXhwIjoyMDgyOTUwNjc5fQ.iWYiUTfKpVnLHEkbhIyvo0fzGxNMMpuRn8UIQZp2u5I"

def inject():
    supabase = create_client(URL, KEY)
    # We use a raw RPC call or we guide the user to the SQL Editor
    print("--- SCHEMA INJECTION REQUIRED ---")
    print("Please paste the following into the Supabase SQL Editor at:")
    print(f"{URL}")
    print("\nCOPY AND RUN THIS SQL:\n")
    print("ALTER TABLE debris_logs ADD COLUMN IF NOT EXISTS forecast_50yr JSONB;")
    print("ALTER TABLE debris_logs ADD COLUMN IF NOT EXISTS market_data JSONB;")
    print("ALTER TABLE debris_logs ADD COLUMN IF NOT EXISTS estimated_value NUMERIC DEFAULT 0;")
    print("\n--------------------------------")

if __name__ == "__main__":
    inject()
