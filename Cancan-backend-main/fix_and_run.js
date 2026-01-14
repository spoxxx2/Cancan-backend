const fs = require('fs');
const { execSync } = require('child_process');

// 1. Fix the JSON formatting
const keyPath = './service-account.json';
const keyData = JSON.parse(fs.readFileSync(keyPath, 'utf8'));
if (keyData.private_key.includes('\\n')) {
    keyData.private_key = keyData.private_key.replace(/\\n/g, '\n');
    fs.writeFileSync(keyPath, JSON.stringify(keyData, null, 2));
    console.log('✅ Key formatting fixed.');
}

// 2. Execute the sync
console.log('Running Sync...');
try {
    const output = execSync('node sync_workspace.js', {
        env: {
            ...process.env,
            SUPABASE_URL: "https://dzrnwzvizztfmjgvpajd.supabase.co",
            SUPABASE_KEY: "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6cm53enZpenp0Zm1qZ3ZwYWpkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NzM3NDY3OSwiZXhwIjoyMDgyOTUwNjc5fQ.iWYiUTfKpVnLHEkbhIyvo0fzGxNMMpuRn8UIQZp2u5I",
            GOOGLE_SHEET_ID: "1HXbi3ePWfOLbmooOB1fCi9ydA6xMviz7jpAj4Vj7Its"
        },
        stdio: 'inherit'
    });
} catch (e) {
    // Error handled by inherit
}
