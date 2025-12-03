import os
from config import load_paths, save_paths

def run(value):
	if value is None:
		print("Usage: python main.py add <folder_path>")
		return
	paths=load_paths()
	if not os.path.exists(value):
		print("Path does not exist.")
	elif value in paths:
		print("Path is already saved.")
	else:
		paths.append(value)
		save_paths(paths)
		print("Path added.")
