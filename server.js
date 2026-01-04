console.log("SUPABASE_URL:", process.env.SUPABASE_URL);
console.log("SUPABASE_KEY (first 12):", process.env.SUPABASE_KEY?.slice(0, 12));process.on("uncaughtException", (err) => {
  console.error("UNCAUGHT EXCEPTION:", err);
});

process.on("unhandledRejection", (err) => {
  console.error("UNHANDLED REJECTION:", err);
});

console.log("SERVER.JS STARTING...");console.log("SERVER.JS STARTING...");require("dotenv").config();
const express = require("express");
const cors = require("cors");
const { createClient } = require("@supabase/supabase-js");

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 3000;

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_KEY
);

app.get("/organism-status", (req, res) => {
  res.json({ ok: true, status: "alive", time: Date.now() });
});

app.post("/system-log", async (req, res) => {
  const { level, module, message, context } = req.body;

  const { data, error } = await supabase
    .from("system_logs")
    .insert([{ level, module, message, context }]);

  if (error) return res.status(500).json({ ok: false, error });
  res.json({ ok: true, data });
});

app.post("/api/cancan", async (req, res) => {
  const { unit, filename, payload } = req.body;

  const { data, error } = await supabase
    .from("field_logs")
    .insert([{ unit, filename, payload }]);

  if (error) return res.status(500).json({ ok: false, error });
  res.json({ ok: true, data });
});

// Admin: list all volunteers
app.get('/admin/volunteers', async (req, res) => {
  const { data, error } = await supabase
    .from('volunteers')
    .select('*')
    .order('created_at', { ascending: false });

  if (error) {
    return res.status(400).json({ success: false, error });
  }

  res.json({ success: true, volunteers: data });
});

console.log("SERVER.JS ABOUT TO LISTEN...");

app.listen(PORT, () => {
  console.log(`SERVER.JS LISTENING ON PORT ${PORT}`);
});