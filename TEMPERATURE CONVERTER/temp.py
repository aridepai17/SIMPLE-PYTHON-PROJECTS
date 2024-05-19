def celsiustofahrenheit(celsius):
    fahrenheit = ( celsius * 9/5 ) + 32
    return fahrenheit

def fahrenheittocelsius(fahrenheit):
    celsius = ( fahrenheit - 32 ) * 5/9
    return celsius

def main():
    while True:
        choice = input("Enter 'C' to convert from Celsius to Fahrenheit.\nEnter 'F' to convert from Fahrenheit to Celsius.\nEnter 'Q' to quit the program.\nEnter your choice: ").upper()
        
        if choice == 'Q':
            break
        
        elif choice == 'C':
            celsius = float ( input ("Enter temperature in Celsius: "))
            fahrenheit = celsiustofahrenheit( celsius )
            print(f"{ celsius }°C is equal to { fahrenheit }°F")
            
        elif choice == 'F':
            fahrenheit = float ( input ("Enter temperature in Fahrenheit: "))
            celsius = fahrenheittocelsius( fahrenheit )
            print(f"{ fahrenheit }°F is equal to { celsius }°C")
            
        else:
            print("Invalid choice. Try again.")
            
if __name__ == "__main__":
    main()