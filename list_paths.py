from config import load_paths

def run():
	paths=load_paths()
	if not paths:
		print("No saved paths.")
	else:
		sorted_paths=sorted(paths)
		for i, p in enumerate(sorted_paths, 1):
			print(f"{i}. {p}")
