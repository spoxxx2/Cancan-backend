const express = require("express");
const cors = require("cors");
const { createClient } = require("@supabase/supabase-js");

const app = express();
app.use(cors());
app.use(express.json({ limit: "10mb" }));

// ------------------------------------------------------------
// SUPABASE CLIENT
// ------------------------------------------------------------
const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_KEY
);

// ------------------------------------------------------------
// ROOT CHECK
// ------------------------------------------------------------
app.get("/", (req, res) => {
  res.json({ ok: true, message: "CANCAN backend alive" });
});

// ------------------------------------------------------------
// ORGANISM STATUS
// ------------------------------------------------------------
app.get("/organism-status", (req, res) => {
  res.json({
    ok: true,
    status: "alive",
    time: Date.now()
  });
});

// ------------------------------------------------------------
// FIELD LOG INGESTION
// ------------------------------------------------------------
app.post("/api/cancan", async (req, res) => {
  try {
    const { unit, filename, payload, received_at } = req.body;

    const { data, error } = await supabase
      .from("field_logs")
      .insert([
        {
          unit,
          filename,
          payload,
          received_at: received_at || Date.now()
        }
      ])
      .select();

    if (error) throw error;

    res.json({ ok: true, data });
  } catch (err) {
    console.error("field_logs error:", err);
    res.status(500).json({ ok: false, error: err.message });
  }
});

// ------------------------------------------------------------
// SYSTEM LOG WRITE
// ------------------------------------------------------------
app.post("/system-log", async (req, res) => {
  try {
    const { level, module, message, context } = req.body;

    const { data, error } = await supabase
      .from("system_logs")
      .insert([
        {
          level,
          module,
          message,
          context
        }
      ])
      .select();

    if (error) throw error;

    res.json({ ok: true, data });
  } catch (err) {
    console.error("system_logs error:", err);
    res.status(500).json({ ok: false, error: err.message });
  }
});

// ------------------------------------------------------------
// SYSTEM LOG LIST
// ------------------------------------------------------------
app.get("/system-log-list", async (req, res) => {
  try {
    const { data, error } = await supabase
      .from("system_logs")
      .select("*")
      .order("timestamp", { ascending: false })
      .limit(200);

    if (error) throw error;

    res.json({ ok: true, data });
  } catch (err) {
    console.error("system-log-list error:", err);
    res.status(500).json({ ok: false, error: err.message });
  }
});

// ------------------------------------------------------------
// START SERVER
// ------------------------------------------------------------
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(\`💚 CANCAN backend running on port \${PORT}\`);
});
