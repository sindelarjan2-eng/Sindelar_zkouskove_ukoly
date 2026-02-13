# Splitting of the entered words
def entered_words(words):
    search_words = []
    word = ""

    for sign in words:
        if sign != " ":
            word += sign
        else:
            if word != "":
                search_words.append(word)
                word = ""

    if word != "":
        search_words.append(word)

    return search_words


# Search for entered words in the text
def find_words(text, search_words):
    found = {}

    for word in search_words:
        found[word] = []

    try:
        with open(text, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line_lower = line.lower()
                for word in search_words:
                    if word in line_lower:
                        found[word].append(line_number)

    except FileNotFoundError:
        print("Error: The specified file was not found.")
        return None

    return found


# Listing of searched words
def list_words(found):
    for word, lines in found.items():
        if lines:
            output = word + " ["

            i = 0
            while i < len(lines):
                output += str(lines[i])
                if i < len(lines) - 1:
                    output += ", "
                i += 1

            output += "]"
            print(output)
        else:
            print(word + " [-]")


# User input 
text = input("Enter the name of the input text: ")
words = input("Enter the searched words (separated by spaces): ").lower()

# Finding of the entered words in the text
search_words = entered_words(words)
found = find_words(text, search_words)

# Printing of founded words
if found is not None:
    list_words(found)
