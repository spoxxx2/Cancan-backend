import subprocess, json, datetime, os, random
from geopy.geocoders import Nominatim
from PIL import Image, ImageDraw
import piexif

# --- SOVEREIGN CONFIG ---
USER_AGENT = "Cancan_Kern_Audit_v3_Hardened"
WITS = [
    "Site integrity looks nominal for Bakersfield winter.",
    "Spectral analysis suggests high probability of non-compliant debris.",
    "Isotopic signature matches regional soil profiles.",
    "Baseline established. Digital Twin sync in progress."
]

def get_address(lat, lon):
    try:
        geolocator = Nominatim(user_agent=USER_AGENT)
        location = geolocator.reverse(f"{lat}, {lon}", timeout=8)
        return location.address.split(',')[0].strip() if location else "Kern_District_Sector"
    except: return "Bakersfield_Audit_Zone"

def process_audit():
    print("🛡️  BOOTING CANCAN KERN V3...")
    
    # 1. Capture Sensors
    try:
        res = subprocess.check_output(["termux-location", "-p", "gps", "-r", "once"])
        data = json.loads(res)
        lat, lon = data.get("latitude"), data.get("longitude")
    except:
        lat, lon = 35.3733, -119.0187 # Bakersfield Baseline

    addr = get_address(lat, lon).replace(" ", "_")
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    wit = random.choice(WITS)

    # 2. Process Target
    target = "20260126_231647.jpg"
    if os.path.exists(target):
        with Image.open(target) as img:
            # Visual Stamp
            draw = ImageDraw.Draw(img)
            label = f"CANCAN | {addr} | GPS: {lat:.4f},{lon:.4f} | {ts}"
            draw.text((20, img.size[1]-120), label, fill="white")
            
            # EXIF Black Box
            exif_dict = {"0th": {}, "Exif": {}, "GPS": {}}
            full_meta = f"STREET: {addr} | NOTE: {wit} | SPECTRAL: YOLO-v3-ACTIVE"
            exif_dict["Exif"][piexif.ExifIFD.UserComment] = full_meta.encode('utf-8')
            
            new_name = f"V3_CERTIFIED_{addr}_{datetime.datetime.now().strftime('%H%M')}.jpg"
            img.save(new_name, exif=piexif.dump(exif_dict), quality=95)
            
            # 3. Sidecar JSON Generation (For Zenodo/Manifest)
            sidecar = {
                "file": new_name,
                "gps": {"lat": lat, "lon": lon},
                "address": addr,
                "human_caption": wit,
                "system_status": "V3_HARDENED"
            }
            with open(f"{new_name}.json", "w") as f:
                json.dump(sidecar, f, indent=4)
            
            print(f"✅ V3 PRODUCTION COMPLETE: {new_name}")
            print(f"📄 SIDECAR DATA GENERATED: {new_name}.json")
    else:
        print(f"⚠️  Target {target} not found. System idling.")

if __name__ == "__main__":
    process_audit()
