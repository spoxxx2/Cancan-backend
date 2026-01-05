import os
import requests

ZENODO_API = "https://zenodo.org/api/deposit/depositions"
record_ids = [18149066, 18149068, 18149070]
TOKEN = os.getenv("ZENODO_TOKEN")
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

for rec_id in record_ids:
    get_url = f"{ZENODO_API}/{rec_id}"
    response = requests.get(get_url, headers=headers)
    if response.status_code != 200:
        print(f"❌ Failed to fetch record {rec_id}")
        continue

    record = response.json()
    bucket_url = record["links"]["bucket"]

    file_path = "placeholder.txt"
    with open(file_path, "rb") as fp:
        filename = os.path.basename(file_path)
        upload_url = f"{bucket_url}/{filename}"
        upload_headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/octet-stream"
        }
        upload_response = requests.put(upload_url, data=fp, headers=upload_headers)
        if upload_response.status_code in [200, 201]:
            print(f"📎 Uploaded placeholder to record {rec_id}")
        else:
            print(f"⚠️ Failed to upload file to record {rec_id}: {upload_response.status_code}")
            continue

    publish_url = f"{get_url}/actions/publish"
    publish_response = requests.post(publish_url, headers=headers)
    if publish_response.status_code == 202:
        print(f"✅ Successfully published record {rec_id}")
    else:
        print(f"❌ Failed to publish record {rec_id}: {publish_response.status_code} {publish_response.json()}")
