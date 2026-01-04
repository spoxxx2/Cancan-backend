// db.js — CANCAN Supabase Connector
// --------------------------------
// PostgreSQL connection module for Supabase backend.
// Safe for Render deployment and Termux dev.

const { Client } = require('pg');

const client = new Client({
  host: process.env.DB_HOST,
  port: process.env.DB_PORT || 5432,
  user: process.env.DB_USER,
  password: process.env.DB_PASS,
  database: process.env.DB_NAME,
  ssl: {
    rejectUnauthorized: false
  }
});

client.connect((err) => {
  if (err) {
    console.error("❌ PostgreSQL connection error:", err);
    return;
  }
  console.log("✅ Connected to Supabase PostgreSQL");
});

module.exports = client;
