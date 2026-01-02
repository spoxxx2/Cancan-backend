const express = require("express");
const cors = require("cors");
const path = require("path");
const { createClient } = require("@supabase/supabase-js");

const app = express();
app.use(cors());
app.use(express.json({ limit: "20mb" }));
app.use(express.static(__dirname));

// --- Supabase client ---
const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_KEY = process.env.SUPABASE_KEY;
const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

// ============================================================
//  FIELD LOG ENDPOINT — CANCAN ORGANISM INPUT
// ============================================================
app.post("/api/cancan", async (req, res) => {
  const entry = {
    ...req.body,
    received_at: Date.now()
  };

  const { data, error } = await supabase
    .from("field_logs")
    .insert([entry]);

  if (error) {
    console.error("Supabase insert error:", error.message);
    return res.json({ ok: false, error: error.message });
  }

  console.log(`💚 Log received from ${entry.unit}: ${entry.filename}`);
  res.json({ ok: true, data });
});

// ============================================================
//  SYSTEM LOGS — INTERNAL ORGANISM MEMORY
// ============================================================
app.post("/system-log", async (req, res) => {
  const { level, module, message, context } = req.body;

  const { data, error } = await supabase
    .from("system_logs")
    .insert([{ level, module, message, context }]);

  if (error) return res.json({ ok: false, error: error.message });
  res.json({ ok: true, log: data[0] });
});

app.get("/system-log-list", async (req, res) => {
  const { data, error } = await supabase
    .from("system_logs")
    .select("*")
    .order("timestamp", { ascending: false })
    .limit(200);

  if (error) return res.json({ ok: false, error: error.message });
  res.json({ ok: true, logs: data });
});

// ============================================================
//  ORGANISM STATUS — SIMPLE HEALTH CHECK
// ============================================================
app.get("/organism-status", async (req, res) => {
  res.json({ ok: true, status: "alive", time: Date.now() });
});

// ============================================================
//  SERVE DASHBOARD
// ============================================================
app.use("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public/index.html"));
});

// ============================================================
//  START SERVER (Render-compatible)
// ============================================================
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`💚 CANCAN backend running on port ${PORT}`);
});
