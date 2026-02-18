class conversion:

    # Setting of the attributes
    def __init__(self):
        pass

    # Binary to hexadecimal conversion function
    def bin_to_hex(self, n):
        n = n.strip()

        # Input validity check
        for sign in n:
            if sign not in "01":
                print("Error: Invalid binary number.")
                exit()

        # Padding zeros from the left to make the length a multiple of 4
        while len(n) % 4 != 0:
            n = "0" + n

        # Binary quads to hexadecimal digit conversion map
        map = {
            "0000": "0", "0001": "1", "0010": "2", "0011": "3",
            "0100": "4", "0101": "5", "0110": "6", "0111": "7",
            "1000": "8", "1001": "9", "1010": "A", "1011": "B",
            "1100": "C", "1101": "D", "1110": "E", "1111": "F"
        }

        hexadecimal = ""

        # Binary to hexadecimal conversion
        for i in range(0, len(n), 4):
            quad = n[i:i+4]
            hexadecimal += map[quad]

        # Removing leading zeros from a number
        while len(hexadecimal) > 1 and hexadecimal[0] == "0":
            hexadecimal = hexadecimal[1:]

        return hexadecimal

    # Hexadecimal to binary conversion function
    def hex_to_bin(self, n):
        n = n.strip().upper()

        # Input validity check
        valid = "0123456789ABCDEF"
        for sign in n:
            if sign not in valid:
                print("Error: Invalid hexadecimal number.")
                exit()

        # Hexadecimal digit to binary quads conversion map
        map = {
            "0": "0000", "1": "0001", "2": "0010", "3": "0011",
            "4": "0100", "5": "0101", "6": "0110", "7": "0111",
            "8": "1000", "9": "1001", "A": "1010", "B": "1011",
            "C": "1100", "D": "1101", "E": "1110", "F": "1111"
        }

        binar = ""

        # Hexadecimal to binary conversion
        for sign in n:
            binar += map[sign]

        # Removing leading zeros from a number
        while len(binar) > 1 and binar[0] == "0":
            binar = binar[1:]

        return binar

def main():
    calculate = conversion()

    # Entering input from the user and outputting the result
    choice = int(input("What will we convert? 1 = from binary to hexadecimal, 2 = from hexadecimal to binary: "))

    if choice == 1:
        bin_cislo = input("Enter a number in binary system: ")
        print("Hexadecimal form:", calculate.bin_to_hex(bin_cislo))

    elif choice == 2:
        hex_cislo = input("Enter a number in hexadecimal system: ")
        print("Binary form:", calculate.hex_to_bin(hex_cislo))

    else:
        print("Incorrect selection parameters entered. Please select option 1 or 2..")
    
if __name__ == "__main__":
    main()