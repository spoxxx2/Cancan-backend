import json
import os
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="cancan_overlord")

def convert_gps_to_address(lat, lon):
    try:
        location = geolocator.reverse(f"{lat}, {lon}")
        return location.address
    except:
        return "Address Translation Offline"

# This logic will now scan your vault for raw GPS logs and "fix" them
VAULT_DIR = "vault/digital_twins"
for file in os.listdir(VAULT_DIR):
    if file.endswith(".json"):
        with open(os.path.join(VAULT_DIR, file), 'r+') as f:
            data = json.load(f)
            if 'gps_coords' in data and 'address' not in data:
                coords = data['gps_coords']
                data['address'] = convert_gps_to_address(coords['lat'], coords['lon'])
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
