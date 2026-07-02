import os
print("=== Science Notes ===")
with open("Science_notes.txt", "r") as file:
    for line in file:
        print(line.strip())
print("===word count===")
with open("Science_notes.txt", "r") as file:
    for line in file:
        words =line.split()
        print(len(words),"words ->",line.strip())
print("=== Merging Notes ===")
if os.path.exists("all notes.txt"):
    print("all notes.txt alraedy exists - overwriting")
else:
    print("all notes.txt not found - creating now")
content = ""
with open("Science_notes.txt", "r") as file:
        content +=  "---Science_notes.txt---\n" 
        content += file.read() + "\n"
        
    