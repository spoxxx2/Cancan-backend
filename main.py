from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn

app = FastAPI()

# Enable CORS so your website can talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/batch-scan")
async def batch_scan(files: List[UploadFile] = File(...), humidity: str = Form(...)):
    total_credits = 0.0
    processed_files = []

    for file in files:
        # Mocking the YOLOv12 + ViT logic for the Digital Twin
        # In 2026, 1 ton of diverted cellulose = ~$21.00
        credit = 17.85 
        total_credits += credit
        
        print(f"SCANNING: {file.filename} | HUMIDITY: {humidity}% | CREDIT: ${credit}")
        processed_files.append(file.filename)

    return {
        "batch_count": len(processed_files),
        "total_credits": f"${total_credits:.2f}",
        "status": "Digital Twins Synced"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
