from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "<h1>Cancan AI Vision Core</h1><p>Status: OPERATIONAL</p>"

@app.route('/analyze')
def analyze():
    # Adaptive Master Strategy: 4-Level Taxonomy
    return jsonify({
        "event": "live_render_test",
        "material": "Polymer",
        "sub_type": "PET #1",
        "condition": "Soiled",
        "forecast_50yr": "High Danger / Zero Worth"
    })

# Note: Gunicorn ignores the block below, but we keep it for local testing
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
