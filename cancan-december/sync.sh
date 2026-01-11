#!/bin/bash
echo "🚀 Hardwiring Identity & SSH..."
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa_cancan || echo "⚠️ SSH Key manual check needed, continuing..."

echo "📦 Staging Digital Twin Metadata (Jan 10)..."
git add .

echo "💾 Committing Strategy..."
git commit -m "Digital Twin Jan 10 Sync: $(date +'%Y-%m-%d %H:%M:%S')"

echo "📡 Pushing to Render/GitHub..."
# Low-memory calibration for IONOS uiserver
git -c core.packedGitLimit=128m -c core.packedGitWindowSize=128m push origin main --force

echo "✅ Sync Complete. Deploying to https://cancan-backend1.onrender.com"
