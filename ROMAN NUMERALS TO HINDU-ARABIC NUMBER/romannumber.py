def romantohinduarabic(roman):
    romanvalues = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000
}
    
    prevvalue = 0
    total = 0
    
    try:
        for char in reversed(roman):
            value = romanvalues[char]
            if value < prevvalue:
                total = total - value
            else:
                total = total + value
            prevvalue = value
    except KeyError:
        print("Invalid roman numeral")

    return total

def main():
    while True:
        try:
            romannumeral = input("Enter a Roman numeral (or type 'exit' to quit): ").strip().upper()
            if romannumeral == 'EXIT':
                break

            hinduarabicnumeral = romantohinduarabic(romannumeral)
            print(f"The Hindu-Arabic equivalent for {romannumeral} is {hinduarabicnumeral}")

        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
