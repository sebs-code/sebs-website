import os
import json

REDIRECTS_FILE = 'redirects.json'
OUTPUT_DIR = 'output'  # or your actual output dir

redirects = [
    {
        "source": "/blog/the%20gruen-transfer-is-consuming-the-internet",
        "status": "301",
        "target": "/blog/the-gruen-transfer-is-consuming-the-internet"
    },
    {
        "source": "/<*>",
        "status": "404-200",
        "target": "/404.html"
    }
]

valid_dirs = ['output', 'output/blog']
invalid_files =  ['index.html', '404.html']

for directory in valid_dirs:
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f not in invalid_files]
    for file in files:
        rel_dir = directory.replace('output', '')
        file = file.replace('.html', '')
        redirects.append({
            "source": f'{rel_dir}/{file}/',
            "target": f'{rel_dir}/{file}',
            "status": "301",
        })                    

with open(REDIRECTS_FILE, 'w') as f:
    json.dump(redirects, f, indent=2)

print(f"Generated {len(redirects)} redirect rules.")
