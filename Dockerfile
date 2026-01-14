# STEP 1: Use a lightweight Python base
FROM python:3.11-slim

# STEP 2: Metadata for 2026 Audit Standard
LABEL vendor="CANCAN Bakersfield"
LABEL status="Golden Overlord"
LABEL uei="SSWWJ3SEMZ73"

# STEP 3: Install Core Dependencies
# We include 'curl' for health checks and 'git' for version audits
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# STEP 4: Set the Command Center
WORKDIR /app

# STEP 5: Inject the Golden Assets
# We copy explicitly to ensure only the site and audit engine are included
COPY index.html .
COPY .nojekyll .
COPY processor.py .

# STEP 6: Environment Security
# Ensures Python output is sent straight to logs without buffering
ENV PYTHONUNBUFFERED=1

# STEP 7: Expose the Heat Map Port
# Port 8080 allows you to view the map locally inside the container
EXPOSE 8080

# STEP 8: Launch Protocol
# Starts a local server to host the Bakersfield Heat Map
CMD ["python3", "-m", "http.server", "8080"]
