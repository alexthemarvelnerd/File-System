import json
import os
DATA_FILE="data.json"
def load_paths():
	if not os.path.exists(DATA_FILE):
		return []
	with open(DATA_FILE,"r") as f:
		return json.load(f)
def save_paths(paths):
	with open(DATA_FILE,"w") as f:
		json.dump(paths,f,indent=4)
