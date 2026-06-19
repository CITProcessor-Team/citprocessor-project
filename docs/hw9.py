# Create a file and write 5 diary entries
with open("my_diary.txt", "w") as f:
    f.write("Today I attended my classes.\n")
    f.write("I studied Python programming.\n")
    f.write("I played cricket with my friends.\n")
    f.write("I listened to some music.\n")
    f.write("I completed my homework.\n")

# Read the file
with open("my_diary.txt", "r") as f:
    lines = f.readlines()

# Count lines
line_count = len(lines)

# Count words
word_count = len(" ".join(lines).split())

# Print counts
print("Number of lines:", line_count)
print("Number of words:", word_count)
