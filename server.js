const express = require("express");
const fs = require("fs");
const path = require("path");
const app = express();

app.use(express.json({ limit: "10mb" }));
app.use(express.static(__dirname));
// --- Directories ---
const LOG_DIR = path.join(__dirname, "logs");
const SUMMARY_DIR = path.join(__dirname, "summaries");

if (!fs.existsSync(LOG_DIR)) fs.mkdirSync(LOG_DIR);
if (!fs.existsSync(SUMMARY_DIR)) fs.mkdirSync(SUMMARY_DIR);

console.log("💚⚡ CANCAN HQ — Neon Pulse Backend v4 ACTIVE");

// ============================================================
//  MAIN ENDPOINT — RECEIVE FIELD LOGS
// ============================================================

app.post("/api/cancan", (req, res) => {
    const data = req.body;

    const entry = {
        timestamp: data.timestamp,
        filename: data.filename,
        unit: data.unit,
        version: data.version,
        signature: data.signature,
        hash: data.hash,
        mood: data.mood,
        received_at: Date.now()
    };

    const filePath = path.join(LOG_DIR, `${entry.timestamp}.json`);
    fs.writeFileSync(filePath, JSON.stringify(entry, null, 2));

    console.log(`💚⚡ [HQ] Log received from ${entry.unit}: ${entry.filename}`);

    res.status(200).send({ status: "ok" });
});

// ============================================================
//  HEARTBEAT ENDPOINT
// ============================================================

app.post("/api/cancan/heartbeat", (req, res) => {
    const hb = {
        unit: req.body.unit,
        timestamp: req.body.timestamp,
        version: req.body.version
    };

    console.log(
        `💚⚡ [heartbeat] ${hb.unit} alive at ${new Date(
            hb.timestamp * 1000
        ).toLocaleTimeString()}`
    );

    res.status(200).send({ status: "alive" });
});

// ============================================================
//  MOOD ENGINE
// ============================================================

function computeMood() {
    const files = fs
        .readdirSync(LOG_DIR)
        .filter((f) => f.endsWith(".json"))
        .sort()
        .slice(-10);

    if (files.length === 0) return "quiet";
    if (files.length > 8) return "high activity";
    if (files.length > 4) return "steady";
    if (files.length > 1) return "light activity";

    return "quiet";
}

// ============================================================
//  DAILY SUMMARY ENGINE
// ============================================================

setInterval(() => {
    const now = new Date();

    if (now.getHours() === 0 && now.getMinutes() === 0) {
        const files = fs
            .readdirSync(LOG_DIR)
            .filter((f) => f.endsWith(".json"));

        const summary = {
            date: now.toDateString(),
            total_logs: files.length,
            mood: computeMood(),
            version: "cancan",
            generated_at: Date.now()
        };

        const filePath = path.join(
            SUMMARY_DIR,
            `summary_${now.toISOString().slice(0, 10)}.json`
        );

        fs.writeFileSync(filePath, JSON.stringify(summary, null, 2));

        console.log("💚⚡ [summary] Daily summary generated");
    }
}, 60000);

// ============================================================
//  DASHBOARD FEED
// ============================================================

app.get("/dashboard/feed", (req, res) => {
    const files = fs
        .readdirSync(LOG_DIR)
        .filter((f) => f.endsWith(".json"))
        .sort()
        .reverse()
        .slice(0, 50);

    const entries = files.map((f) => {
        const raw = fs.readFileSync(path.join(LOG_DIR, f));
        return JSON.parse(raw);
    });

    res.json({
        entries,
        mood: computeMood(),
        version: "cancan"
    });
});

// ============================================================
//  START SERVER
// ============================================================

app.listen(3000, () => {
    console.log("💚⚡ CANCAN HQ listening on port 3000");
});
