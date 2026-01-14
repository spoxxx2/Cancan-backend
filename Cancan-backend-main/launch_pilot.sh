#!/bin/bash

echo "--- CANCAN System Activation: Arvin Pilot ---"

# 1. Verify Database Connection (Nervous System)
echo "[1/3] Checking Supabase Connectivity..."
node -e "require('./db.js').any('SELECT 1').then(() => console.log('SUPABASE: LIVE')).catch(err => { console.error('CONNECTION FAILED:', err); exit(1); })"

# 2. Upload DOI Metadata (Academic Engine)
echo "[2/3] Staging Arvin Pilot DOI to Zenodo..."
# Using your existing upload script found in your directory
python3 upload_dois.py --title 'CANCAN Arvin Pilot Program Baseline' --folder './logs'

# 3. Update Pilot Tracker (The Lungs)
echo "[3/3] Updating Website Pilot Tracker..."
# This updates the status on your index.html file
sed -i 's/Field Data Collection (In Progress)/Phase 1: Active Deployment/g' index.html

echo "--- Launch Sequence Complete ---"
