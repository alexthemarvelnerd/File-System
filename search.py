import os
from config import load_paths
def run(keyword,extension):
	paths=load_paths()
	found_files=[]
	for p in paths:
		if os.path.exists(p):
			for root, dirs, files in os.walk(p):
				for file in files:
					name_match=keyword in file.lower()
					ext_match=True
					if extension is not None:
						ext_match=file.lower().endswith(extension)
					if name_match and ext_match:
						full_path=os.path.join(root,file)
						found_files.append(full_path)
	if not found_files:
		print("No matching files found.")
	else:
		found_files.sort()
		for f in found_files:
			print(f)
