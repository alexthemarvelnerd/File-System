import sys
import add
import list_paths
import scan
import search
import remove

if len(sys.argv)<2:
	print("Commands: add, list, scan, search, remove")
	sys.exit()
command=sys.argv[1].lower()
value1=None
value2=None
if len(sys.argv) >= 3:
	value1=sys.argv[2]
if len(sys.argv) >= 4:
	value2=sys.argv[3]
if command=="add":
	add.run(value1)
elif command=="list":
	list_paths.run()
elif command=="scan":
	scan.run(value1)
elif command=="search":
	if value1 is None:
		print("Usage: python main.py search <keyword> [extension]")
	else:
		search.run(value1, value2)
elif command=="remove":
	remove.run(value1)
else:
	print("Invalid command.")
