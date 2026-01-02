const express = require("express");
const multer = require("multer");
const mysql = require("mysql2");
const fs = require("fs");
const axios = require("axios");
const path = require("path");

const app = express();
const upload = multer({ dest: "/tmp" });

// TODO: Replace with your real OpenAI API key
const OPENAI_API_KEY = "YOUR_OPENAI_KEY_HERE";

// MySQL connection (IONOS)
const db = mysql.createConnection({
  host: "db5019309070.hosting-data.io",
  user: "dbu900517",
  password: "YOUR_DB_PASSWORD_HERE",
  database: "dbs15128735",
  port: 3306,
});

db.connect((err) => {
  if (err) {
    console.error("MySQL connection error:", err);
  } else {
    console.log("MySQL connected.");
  }
});

app.use(express.json());

app.post("/analyze-photo", upload.single("file"), async (req, res) => {
  try {
    const { lat, lon, timestamp } = req.body;

    if (!req.file) {
      return res.status(400).json({ error: "No file uploaded" });
    }

    const photoPath = req.file.path;
    const base64Image = fs.readFileSync(photoPath, { encoding: "base64" });

    // Send to OpenAI Vision
    const aiResponse = await axios.post(
      "https://api.openai.com/v1/chat/completions",
      {
        model: "gpt-4-vision-preview",
        messages: [
          {
            role: "system",
            content:
              "You are a civic field analyst. Return STRICT JSON with keys: category, severity, short_note, long_description, escalated (boolean), tags (array). No extra text.",
          },
          {
            role: "user",
            content: [
              { type: "text", text: "Analyze this photo and return JSON only." },
              {
                type: "image_url",
                image_url: {
                  url: `data:image/jpeg;base64,${base64Image}`,
                },
              },
            ],
          },
        ],
        max_tokens: 800,
      },
      {
        headers: {
          Authorization: `Bearer ${OPENAI_API_KEY}`,
          "Content-Type": "application/json",
        },
      }
    );

    const aiText = aiResponse.data.choices[0].message.content.trim();

    let parsed;
    try {
      parsed = JSON.parse(aiText);
    } catch (e) {
      console.error("AI JSON parse error:", aiText);
      return res.status(500).json({ error: "AI JSON parse error", raw: aiText });
    }

    const {
      category,
      severity,
      short_note,
      long_description,
      escalated,
      tags,
    } = parsed;

    const photo_url = `/uploads/${path.basename(photoPath)}`;
    const thumb_url = photo_url; // placeholder

    const sql = `
      INSERT INTO logs (
        timestamp, lat, lon, category, severity,
        short_note, long_description, photo_url, thumb_url,
        tags, escalated
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `;

    const values = [
      timestamp || new Date(),
      lat || null,
      lon || null,
      category || null,
      severity || null,
      short_note || null,
      long_description || null,
      photo_url,
      thumb_url,
      JSON.stringify(tags || []),
      escalated ? 1 : 0,
    ];

    db.execute(sql, values, (err) => {
      if (err) {
        console.error("SQL error:", err);
        return res.status(500).json({ error: "Database error" });
      }

      return res.json({
        status: "ok",
        category,
        severity,
        short_note,
        long_description,
      });
    });
  } catch (err) {
    console.error("AI or upload error:", err);
    return res.status(500).json({ error: "AI or upload error" });
  } finally {
    if (req.file && req.file.path) {
      fs.unlink(req.file.path, () => {});
    }
  }
});

// Required for Passenger on IONOS
