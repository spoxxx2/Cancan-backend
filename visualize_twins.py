import os
import json
import matplotlib.pyplot as plt
from collections import Counter

VAULT_DIR = "vault/digital_twins"
materials = []
impact_scores = []

for file in os.listdir(VAULT_DIR):
    if file.endswith(".json"):
        with open(os.path.join(VAULT_DIR, file), 'r') as f:
            data = json.load(f)
            materials.append(data['objects'][0]['material'])
            impact_scores.append(data['environmental_impact_score'])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

counts = Counter(materials)
ax1.bar(counts.keys(), counts.values(), color='skyblue')
ax1.set_title('Bakersfield Material Distribution')
ax1.set_ylabel('Audit Count')

ax2.hist(impact_scores, bins=10, color='lightgreen', edgecolor='black')
ax2.set_title('Environmental Impact Distribution')
ax2.set_xlabel('Score (out of 100)')

plt.tight_layout()
plt.savefig('audit_visualization.png')
print("Visualization saved as audit_visualization.png")
