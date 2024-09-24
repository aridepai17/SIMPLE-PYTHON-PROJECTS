import re

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}

def text_to_morse(text):
    """
    Converts the input text to Morse code.
    """
    morse_code = ""
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
        elif char == " ":
            morse_code += "/ "
    return morse_code.strip()

def morse_to_text(morse_code):
    """
    Converts the input Morse code to text.
    """
    text = ""
    morse_chars = morse_code.strip().split()
    for morse_char in morse_chars:
        if morse_char == "/":
            text += " "
        else:
            for key, value in MORSE_CODE_DICT.items():
                if value == morse_char:
                    text += key
    return text

def main():
    print("Welcome to the Morse Code Translator!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Convert text to Morse code")
        print("2. Convert Morse code to text")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            text = input("Enter the text to convert to Morse code: ")
            print(f"Morse code: {text_to_morse(text)}")
        elif choice == "2":
            morse_code = input("Enter the Morse code to convert to text: ")
            print(f"Text: {morse_to_text(morse_code)}")
        elif choice == "3":
            print("Thank you for using the Morse Code Translator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()