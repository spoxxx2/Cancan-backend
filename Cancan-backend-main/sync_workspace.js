const { google } = require('googleapis');
const { createClient } = require('@supabase/supabase-js');

async function syncToSheet() {
  // 1. Setup Supabase
  const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);
  
  // 2. Setup Google Auth
  const auth = new google.auth.GoogleAuth({
    keyFile: 'service-account.json',
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
  });

  const sheets = google.sheets({ version: 'v4', auth });
  const spreadsheetId = process.env.GOOGLE_SHEET_ID;

  // 3. Pull latest log
  const { data: logs, error } = await supabase
    .from('system_logs')
    .select('created_at, level, message')
    .order('created_at', { ascending: false })
    .limit(1);

  if (error) throw error;

  if (logs && logs.length > 0) {
    await sheets.spreadsheets.values.append({
      spreadsheetId,
      range: 'Sheet1!A:C',
      valueInputOption: 'USER_ENTERED',
      resource: { values: [[logs[0].created_at, logs[0].level, logs[0].message]] },
    });
    console.log('✅ SYNC COMPLETE: Arvin Log moved to Google Sheets.');
  }
}

syncToSheet().catch(err => console.error('❌ Sync Error:', err.message));
