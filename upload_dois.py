import requests

ZENODO_URL = "https://zenodo.org/api/deposit/depositions"
import os
TOKEN = os.getenv("ZENODO_TOKEN")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

dois = [
    {
        "title": "Decentralized Identity Verification Using Supabase and Next.js",
        "description": "A technical exploration of secure, scalable identity systems for modern web applications.",
        "creators": [{"name": "Canfield, Casey", "affiliation": "Cancan Inc."}]
    },
    {
        "title": "Edge-First Architectures for Real-Time Admin Gatekeeping",
        "description": "A performance study on cookie-based SSR authentication in serverless environments.",
        "creators": [{"name": "Canfield, Casey", "affiliation": "Cancan Inc."}]
    },
    {
        "title": "Simulated Data Streams for AI-Driven Access Control Testing",
        "description": "A framework for generating synthetic user sessions to validate admin route protection.",
        "creators": [{"name": "Canfield, Casey", "affiliation": "Cancan Inc."}]
    }
]

for entry in dois:
    metadata = {
        "metadata": {
            "title": entry["title"],
            "upload_type": "publication",
            "publication_type": "article",
            "description": entry["description"],
            "creators": entry["creators"]
        }
    }

    response = requests.post(ZENODO_URL, json=metadata, headers=headers)
    print(response.status_code, response.json())