import os
import time
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

ZENODO_API = "https://zenodo.org/api/deposit/depositions"
TOKEN = os.getenv("ZENODO_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

WATCH_DIR = "/storage/emulated/0/DCIM/Camera"

def get_gps_coords(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return None
        gps_info = {}
        for tag, value in exif_data.items():
            decoded = TAGS.get(tag)
            if decoded == "GPSInfo":
                for t in value:
                    sub_decoded = GPSTAGS.get(t)
                    gps_info[sub_decoded] = value[t]
        if not gps_info:
            return None
        def convert(coord, ref):
            d, m, s = coord
            degrees = d[0] / d[1] + m[0] / m[1] / 60 + s[0] / s[1] / 3600
            return degrees if ref in ['N', 'E'] else -degrees
        lat = convert(gps_info["GPSLatitude"], gps_info["GPSLatitudeRef"])
        lon = convert(gps_info["GPSLongitude"], gps_info["GPSLongitudeRef"])
        return (lat, lon)
    except:
        return None

def generate_caption(filename, gps=None):
    caption = f"Photo captured: {filename}"
    if gps:
        caption += f" at location ({gps[0]:.5f}, {gps[1]:.5f})"
    return caption

def upload_to_zenodo(file_path):
    r = requests.post(ZENODO_API, json={}, headers=HEADERS)
    if r.status_code != 201:
        print(f"❌ Failed to create deposition: {r.status_code}")
        return
    deposition = r.json()
    bucket_url = deposition["links"]["bucket"]
    filename = os.path.basename(file_path)

    with open(file_path, "rb") as fp:
        upload_url = f"{bucket_url}/{filename}"
        r = requests.put(upload_url, data=fp, headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/octet-stream"
        })
        if r.status_code not in [200, 201]:
            print(f"❌ Upload failed: {r.status_code}")
            return

    gps = get_gps_coords(file_path)
    caption = generate_caption(filename, gps)
    metadata = {
        "metadata": {
            "title": caption,
            "upload_type": "image",
            "description": caption,
            "creators": [{"name": "SpoX1"}],
            "access_right": "open",
            "license": "cc-by"
        }
    }

    r = requests.put(f"{ZENODO_API}/{deposition['id']}", json=metadata, headers=HEADERS)
    if r.status_code != 200:
        print(f"⚠️ Metadata update failed: {r.status_code}")
        return

    r = requests.post(f"{ZENODO_API}/{deposition['id']}/actions/publish", headers=HEADERS)
    if r.status_code == 202:
        print(f"✅ Published {filename} to Zenodo")
    else:
        print(f"❌ Failed to publish: {r.status_code} {r.json()}")

class PhotoHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.lower().endswith((".jpg", ".jpeg", ".png")):
            print(f"📸 New photo detected: {event.src_path}")
            time.sleep(1.5)
            upload_to_zenodo(event.src_path)

if __name__ == "__main__":
    print(f"👀 Watching {WATCH_DIR} for new photos...")
    observer = Observer()
    observer.schedule(PhotoHandler(), path=WATCH_DIR, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
