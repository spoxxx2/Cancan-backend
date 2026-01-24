import hashlib
import os
import json

VAULT_DIR = "vault/digital_twins/"
MANIFEST_FILE = "manifest.sha256"

def generate_file_hash(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def seal_vault():
    manifest = {}
    print("--- SEALING VAULT ---")
    for filename in os.listdir(VAULT_DIR):
        if filename.endswith((".json", ".jpg")):
            path = os.path.join(VAULT_DIR, filename)
            file_hash = generate_file_hash(path)
            manifest[filename] = file_hash
            print(f"Hashed: {filename}")

    with open(MANIFEST_FILE, "w") as f:
        json.dump(manifest, f, indent=4)
    print(f"VAULT SEALED: {MANIFEST_FILE} updated.")

if __name__ == "__main__":
    seal_vault()
