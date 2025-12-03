import os
from config import load_paths
def run(extension):
	paths=load_paths()
	sorted_paths=sorted(paths)
	for p in sorted_paths:
		if os.path.exists(p):
			count=0
			for root, dirs, files in os.walk(p):
				for file in files:
					if extension is None:
						count += 1
					else:
						if file.lower().endswith(extension):
							count+=1
			if extension is None:
				print(f"{p} -> {count} total files")
			else:
				print(f"{p} -> {count} '{extension}' files")
		else:
			print("Missing path:",p)
 
