const { Client } = require('pg');

// Using Direct Connection (Port 6543) to avoid Pooler issues
const connectionString = "postgresql://postgres:F4A5HSyqQdzsBLCa@db.dzrnwzvizztfmjgvpajd.supabase.co:6543/postgres";

const client = new Client({
  connectionString: connectionString,
  ssl: { rejectUnauthorized: false }
});

// We will handle the connection inside the query calls to be safe
module.exports = client;
