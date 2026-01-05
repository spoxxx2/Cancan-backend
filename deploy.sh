#!/bin/bash

echo "🚀 Starting full-stack deployment for Cancan Kern..."

# 1. Sync frontend
echo "📦 Uploading frontend to server..."
rsync -avz --delete ./public/ your_user@your_host:/var/www/cancankern.org/

# 2. Deploy backend if exists
if [ -d backend ]; then
  echo "🧠 Deploying backend functions..."
  cd backend
  if [ -f supabase/config.toml ]; then
    supabase functions deploy all
  else
    echo "⚠️ No Supabase config found. Skipping backend deployment."
  fi
  cd ..
else
  echo "⚠️ No backend directory found. Skipping backend deployment."
fi

# 3. Apply DB schema if exists
if [ -d db ]; then
  echo "🗃️ Applying database schema..."
  cd db
  if [ -f schema.sql ]; then
    psql "$DATABASE_URL" < schema.sql
  else
    echo "⚠️ No schema.sql found. Skipping DB migration."
  fi
  cd ..
else
  echo "⚠️ No db directory found. Skipping DB migration."
fi

# 4. Git commit and push if repo
if [ -d .git ]; then
  echo "📤 Committing changes to GitHub..."
  git add .
  git commit -m "Full deploy: frontend + backend + db"
  git push origin main
else
  echo "⚠️ Not a Git repository. Skipping Git push."
fi

echo "✅ Deployment complete. Cancan Kern is live!"
