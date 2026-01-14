#!/bin/bash

echo "[SYSTEM] Initializing Pilot Program 2..."
echo "[LOG] Starting FastAPI Backend (Port 8000)..."

# Start the Python backend in the background
python main.py > backend.log 2>&1 &
BACKEND_PID=$!

echo "[LOG] Starting Web Dashboard (Port 8080)..."
echo "[URL] Access at: http://localhost:8080"

# Start the web server in the foreground
python -m http.server 8080

# When you stop the web server (Ctrl+C), kill the backend too
trap "kill $BACKEND_PID; echo 'System Shutdown'; exit" SIGINT SIGTERM
