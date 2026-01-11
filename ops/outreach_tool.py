import json

def list_leads():
    try:
        with open('ops/buyer_leads.json', 'r') as f:
            leads = json.load(f)
        
        print("\n--- CANCANKERN TARGET ACQUISITION LIST ---")
        for category, contacts in leads.items():
            print(f"\n[Category: {category.upper()}]")
            for lead in contacts:
                print(f" - {lead['name']} | {lead['contact']}")
                print(f"   Focus: {lead['interest']}")
        print("\nReady to send Prospectus.")
    except Exception as e:
        print(f"❌ Lead Vault Error: {e}")

if __name__ == "__main__":
    list_leads()
