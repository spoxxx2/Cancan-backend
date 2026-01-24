#include <iostream>
#include <fstream>

int main() {
    std::ofstream site("index.html");
    site << "<!DOCTYPE html>\n<html lang='en'>\n<head>"
         << "<meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>"
         << "<style>"
         << "body { background:#0a0a0a; color:#00ff41; font-family:'Courier New', monospace; padding:20px; line-height:1.4; }"
         << ".compliance-header { border: 2px solid #00ff41; padding:20px; margin-bottom:20px; background:#111; }"
         << ".badge-row { display: flex; gap: 10px; margin-top: 10px; flex-wrap: wrap; }"
         << ".badge { background:#00ff41; color:#000; padding:5px 10px; font-weight:bold; text-decoration:none; font-size:0.8em; }"
         << ".license-box { border: 1px dashed #555; padding: 15px; margin-top: 30px; font-size: 0.85em; background: #050505; }"
         << "h2 { border-left: 5px solid #00ff41; padding-left: 10px; color: #fff; }"
         << "</style></head><body>"
         
         << "<div class='compliance-header'>"
         << "<h1>CANCANKERN ZENITH NODE 001</h1>"
         << "<p><b>SAM UEI:</b> SSWWJ3SEMZ73 | <b>EIN:</b> 39-2361270</p>"
         << "<div class='badge-row'>"
         << "<a href='https://github.com/spoxxx2/cancankern-org/releases/tag/v1.5.0' class='badge'>GITHUB v1.5.0 RELEASE</a>"
         << "<a href='https://zenodo.org/communities/cancankern' class='badge'>ZENODO ARCHIVE</a>"
         << "</div>"
         << "</div>"

         << "<h2>📊 Multi-Modal Dataset</h2>"
         << "<p>318 High-Fidelity Waste Audits from 1501 Pearl St. Includes Panoptic Segmentation data and 100-year oxidation matrices for Ferrous/Polymer materials.</p>"

         << "<h2>⚖️ Data Licensing Agreement</h2>"
         << "<div class='license-box'>"
         << "<b>CC-BY-NC-SA 4.0 (Non-Commercial):</b> Free for academic and non-profit use.<br><br>"
         << "<b>Commercial License:</b> For LLM/Vision training or proprietary carbon credit models, a commercial licensing fee applies. Contact <i>licensing@cancankern.org</i> for bulk JSON access."
         << "</div>"

         << "<h2>🪰 Bio-Acoustic BSFL Pilot</h2>"
         << "<p>Real-time frequency monitoring of Black Soldier Fly Larvae for rapid organic digestion. Compliance with SB 1383 mandates.</p>"

         << "<footer>© 2026 CANCANKERN™ | DOI: Pending Issuance (Zenodo Archive)</footer>"
         << "</body></html>";
    site.close();
    return 0;
}
