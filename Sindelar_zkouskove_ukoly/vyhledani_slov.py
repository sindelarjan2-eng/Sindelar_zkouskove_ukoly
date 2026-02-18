class Find_in_the_text:

    # Setting of the attributes
    def __init__(self, file, words):
        self.name = file
        self.search_words = self.entered_words(words.lower())
        self.found = {}

    # Splitting of the entered words
    def entered_words(self, words):
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
    def find_words(self):

        for word in self.search_words:
            self.found[word] = []

        try:
            with open(self.name, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    line_lower = line.lower()
                    for word in self.search_words:
                        if word in line_lower:
                            self.found[word].append(line_number)

        except FileNotFoundError:
            print("Error: The specified file was not found.")
            return None

        return self.found


    # Listing of searched words
    def list_words(self):
        for word, lines in self.found.items():
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

def main():
    # User input 
    text = input("Enter the name of the input text: ")
    words = input("Enter the searched words (separated by spaces): ").lower()

    # Creating class object
    search = Find_in_the_text(text, words)

    # Finding of the entered words in the text
    found = search.find_words()

    # Printing of founded words
    if found is not None:
        search.list_words()

if __name__ == "__main__":
    main()