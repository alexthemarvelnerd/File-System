from config import load_paths, save_paths

def run(value):
	if value is None:
		print("Usage: python main.py remove <number>")
		return
	if value.isdigit():
		index=int(value)-1
		paths=load_paths()
		if index >= 0 and index < len(paths):
			removed=paths.pop(index)
			save_paths(paths)
			print("Removed:", removed)
		else:
			print("Number not in list.")
	else:
		print("Please enter a valid number.")
