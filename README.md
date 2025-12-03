This project is intended to allow the user to manage and search through multiple folder paths at once. The user can add folders, list them,
scan how many files they contain, search for files by name, and remove folders from the list.

Below is a list of commands you would use
You would add a folder by using this command in terminal- python main.py add (some path)
List saved folders - python main.py list
Scan folders for file count - python main.py scan
Scan only specific file type - python main.py scan (filetype name)
Search for a file - python main.py search (file name)
File with specific extension - python main.py search (file name.file type)
Remove saved folder - python main.py remove (folder)

main.py - reads the command from the terminal and sends the request to the correct file.
config.py - handles saving and loading the folder paths with a JSON file.
add.py - adds a new folder path, and prevents duplicates if the path exists
list_paths.py - displays all saved folder paths in sorted order and labels them with numbers
scan.py - counts how many files exist in each saved folder. 
search.py - searches through all saved folders for a file that matches a keyword.
remove.py - removes a folder from the saved list.
data.json - stores all saved paths in a list. Updates every time paths are added or removed.
