#include <iostream>
#include <fstream>

int main() {
    std::ofstream site("index.html");
    site << "<!DOCTYPE html>\n<html><head><style>"
         << "body { background:#0a0a0a; color:#00ff41; font-family:'Courier New'; padding:20px; }"
         << ".compliance-header { border: 2px solid #00ff41; padding:15px; margin-bottom:20px; text-align:center; }"
         << ".release-badge { background:#00ff41; color:#000; padding:5px; font-weight:bold; text-decoration:none; }"
         << "h2 { border-bottom: 1px solid #333; padding-bottom:10px; }"
         << "</style></head><body>"
         << "<div class='compliance-header'>"
         << "<h1>CANCANKERN ZENITH NODE 001</h1>"
         << "<p><b>SAM UEI:</b> SSWWJ3SEMZ73 | <b>EIN:</b> 39-2361270</p>"
         << "<a href='https://github.com/spoxxx2/cancankern-org/releases/tag/v1.5.0' class='release-badge'>VERIFIED RELEASE v1.5.0</a>"
         << "</div>"
         << "<h2>🔍 Audit Vault</h2><p>318 Validated Digital Twins with 100-year decay matrices.</p>"
         << "<h2>🍎 FRO Compliance</h2><p>Authorized Third-Party Compliance Auditor (BMC § 8.32.190).</p>"
         << "<h2>🪰 BSFL Pilot</h2><p>Bio-Acoustic Monitoring Active at 1501 Pearl St.</p>"
         << "<footer>© 2026 CANCANKERN™ | Bakersfield, CA</footer>"
         << "</body></html>";
    site.close();
    return 0;
}
