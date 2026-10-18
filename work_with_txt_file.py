"""
This is a tutorial about files - txt & json in Back-End development.

Why we use files in Back-End:
1. Configuration files: Back-end systems use files to store sensitive settings or env vars
   like DB address, server ports, encryption keys.
2. Logging: This involves recording events, errors, and user actions in text files (.txt)
   or structured files.
3. Data interchange: Back-end APIs receive and return data typically in JSON format
   (like dictionaries).

The 3 File Modes:
1. 'r' - Read from file. Impossible to change. If the file doesn't exist, it throws an error (handled via try-except).
2. 'w' - Write to file. Always starts from the beginning and deletes the old file content.
3. 'a' - Append to file. Like an update; gets the file from the last character and continues to add text.
* Note: In 'w' and 'a' modes, if the file doesn't exist, Python will create a new file in the path.
"""

file_path = "app_settings.txt"

# 1. Creating a new file in 'w' mode (Initial write) with error handling
try:
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Hello World\n")
    print("File created successfully and first line added!")
except IOError as e:
    print(f"Error writing to file: {e}")


# 2. Overwriting the file in 'w' mode with configuration data
try:
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("HOST=127.0.0.1\n")
        file.write("PORT=8080\n")
        file.write("DEBUG=True\n")
    print("File updated: deleted old text and added these 3 lines.")
except IOError as e:
    print(f"Error updating file: {e}")


# 3. Appending new text to the end of the file in 'a' mode (Append)
try:
    with open(file_path, "a", encoding="utf-8") as file:
        file.write("ENV=production\n")
        file.write("We are hackers of HackerU\n")
    print("New lines added to the end of the file successfully!")
except IOError as e:
    print(f"Error appending to file: {e}")


# 4. Reading the file in 'r' mode (Read) with safety checks
"""
Reading methods overview:
- file.read()     - Read all file content as one long string.
- file.readline() - Read one line at a time (from begin until \n).
- file.readlines()- Read all lines and return them as a list of strings (each line is an element).
"""
try:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(f"\n--- Data from file: {file_path} ---")

        # Using enumerate to display a serial line number for each row
        for line_num, line in enumerate(lines, 1):
            print(f"{line_num}. {line.strip()}")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except IOError as e:
    print(f"Error reading file: {e}")

