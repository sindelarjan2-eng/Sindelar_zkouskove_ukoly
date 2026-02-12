# Enter of the input from the user
text = input("Enter the name of the input text: ")
words = input("Enter the searched words (separated by spaces): ").lower().split()

# Dictionary for storing found lines for each word
found = {word: [] for word in words}

# Search for entered words in the text
try:
    with open(text, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line_lower = line.lower()
            for slovo in words:
                if slovo in line_lower:
                    found[slovo].append(line_number)
except FileNotFoundError:
    print("Error: The specified file was not found.")
    exit()

# Listing of searched words
for word, lines in found.items():
    if lines:
        print(f"{word} [{', '.join(map(str, lines))}]")
        found_any = True
    else:
        print(f"{word} [-]")