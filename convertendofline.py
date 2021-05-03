# Convert line endings in-place 

import os

# replacement strings
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

# relative or absolute file path, e.g.:
file_path = r"c:\Users\Username\documents"

for file in os.listdir(file_path):
    if file.endswith(".txt"):
        print(file)

        with open(file, 'rb') as open_file:
            content = open_file.read()
    
        content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

        with open(file, 'wb') as open_file:
            open_file.write(content)
