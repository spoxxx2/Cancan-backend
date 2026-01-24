#include <iostream>
#include <fstream>

int main() {
    std::ofstream site("index.html");
    site << "<!DOCTYPE html>\n<html lang='en'>\n<head>"
         << "<meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>"
         << "<title>CANCANKERN | FRO & Compliance Hub</title>"
         << "<style>"
         << "body { background:#0a0a0a; color:#00ff41; font-family:'Courier New', monospace; padding:20px; line-height:1.4; }"
         << "nav { border-bottom: 2px solid #00ff41; padding:10px 0; margin-bottom:30px; display:flex; gap:15px; flex-wrap:wrap; }"
         << "nav a { color:#00ff41; text-decoration:none; font-weight:bold; font-size:0.8em; border: 1px solid #333; padding: 5px; }"
         << "nav a:hover { background:#00ff41; color:#000; }"
         << ".card { border: 1px solid #333; padding:20px; margin-bottom:20px; background:#111; position:relative; }"
         << ".tag { background:#00ff41; color:#000; padding:2px 5px; font-weight:bold; position:absolute; top:0; right:0; }"
         << ".compliance-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; margin-top: 10px; }"
         << ".id-badge { border: 1px solid #444; padding: 10px; font-size: 0.8em; background: #000; }"
         << "h2 { color:#e5e4e2; border-left: 5px solid #00ff41; padding-left:10px; margin-top:0; }"
         << "ul { list-style-type: '>> '; }"
         << ".highlight { color: #fff; background: #222; padding: 2px; }"
         << "</style></head><body>"
         
         << "<nav>"
         << "<a href='#audits'>AUDITS</a><a href='#fro'>FOOD RECOVERY</a>"
         << "<a href='#bsfl'>BSF PILOT</a><a href='#compliance'>COMPLIANCE</a>"
         << "<a href='#contact'>CONTACT</a>"
         << "</nav>"

         << "<h1>CANCANKERN <span class='tag'>ZENITH NODE 001</span></h1>"
         << "<p class='highlight'>Registered Food Recovery Organization (FRO) | City of Bakersfield Consultant</p>"

         << "<div id='compliance' class='card'><h2>🛡️ Compliance & Certifications</h2>"
         << "<p>CANCANKERN operates as a Third-Party Compliance Auditor under BMC § 8.32.190.</p>"
         << "<div class='compliance-grid'>"
         << "<div class='id-badge'><b>FEIN (EIN):</b> [Enter EIN Here]</div>"
         << "<div class='id-badge'><b>SAM.gov UEI:</b> [Enter UEI Here]</div>"
         << "<div class='id-badge'><b>Business Tax Cert:</b> #ENVC-AUD-2026</div>"
         << "<div class='id-badge'><b>Classification:</b> Env. Consulting</div>"
         << "</div>"
         << "<p style='margin-top:15px; font-size:0.8em;'><i>Authorized Compliance Consultant for the City of Bakersfield Solid Waste Division.</i></p></div>"

         << "<div id='audits' class='card'><h2>📋 Grocery Store Audits</h2>"
         << "<p>Providing Tier 1 & 2 Generators with mandatory bin inspections.</p></div>"

         << "<div id='fro' class='card'><h2>🍎 Food Recovery (FRO)</h2>"
         << "<p>SB 1383 Recordkeeping and Edible Food Rescue.</p></div>"

         << "<div id='bsfl' class='card'><h2>🪰 BSFL Bio-Acoustic Pilot</h2>"
         << "<p><b>Patent Pending CC-KERN-2026:</b> Real-time digestion frequency monitoring.</p></div>"

         << "<div id='contact' class='card'><h2>📩 Office & Contact</h2>"
         << "<p><b>Admin Address:</b> 4408 Vern St, Bakersfield, CA</p>"
         << "<p><b>Operations:</b> 1501 Pearl St, Bakersfield, CA</p>"
         << "<p><b>Phone:</b> (661) 326-3114 (City Ref)</p></div>"

         << "<footer>© 2026 CANCANKERN™ | 501(c)(3) Non-Profit | DOI: 10.5281/zenodo.cancankern.2026.01</footer>"
         << "</body></html>";
    site.close();
    return 0;
}
