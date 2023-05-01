import requests
import os

source_url = "https://raw.githubusercontent.com/MichelangeloHimself/CrystalMetricDex/main/data/pokemon/dex_entries/"
current_dir = os.getcwd()
dest_dir = os.path.join(current_dir, "data/pokemon/dex_entries") # Look for the directory in the current working directory

for filename in os.listdir(dest_dir):
    source_file = source_url + filename
    dest_file = os.path.join(dest_dir, filename)
    
    response = requests.get(source_file)
    
    with open(dest_file, 'w') as f:
        f.write(response.text)
    
    print(f"Updated {dest_file}")
