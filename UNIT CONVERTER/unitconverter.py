def unitconversion():
    print("UNIT CONVERTER")
    print("1. Kilometers to Miles.")
    print("2. Miles to Kilometers.")
    print("3. Celsius to Fahrenheit.")
    print("4. Fahrenheit to Celsius.")
    print("5. Celsius to Kelvin.")
    print("6. Kilograms to Pounds.")
    print("7. Pounds to Kilograms.")
    print("8. Kilograms to Grams.")
    print("9. Grams to Kilograms.")
    print("10. Feet to Meters.")
    print("11. Meters to Feet.")
    print("12. Liters to Gallons.")
    print("13. Gallons to Liters.")

    choice = input("Enter your choice: ")

    if choice == '1':
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} kilometers is equal to {miles} miles.")
    elif choice == '2':
        miles = float(input("Enter distance in miles: "))
        km = miles / 0.621371
        print(f"{miles} miles is equal to {km} kilometers.")
    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
    elif choice == '4':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
    elif choice == '5':
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius} degrees Celsius is equal to {kelvin} Kelvin.")
    elif choice == '6':
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kilograms is equal to {pounds} pounds.")
    elif choice == '7':
        pounds = float(input("Enter weight in pounds: "))
        kg = pounds / 2.20462
        print(f"{pounds} pounds is equal to {kg} kilograms.")
    elif choice == '8':
        kg = float(input("Enter weight in kilograms: "))
        grams = kg * 1000
        print(f"{kg} kilograms is equal to {grams} grams.")
    elif choice == '9':
        grams = float(input("Enter weight in grams: "))
        kg = grams / 1000
        print(f"{grams} grams is equal to {kg} kilograms.")
    elif choice == '10':
        feet = float(input("Enter length in feet: "))
        meters = feet * 0.3048
        print(f"{feet} feet is equal to {meters} meters.")
    elif choice == '11':
        meters = float(input("Enter length in meters: "))
        feet = meters / 0.3048
        print(f"{meters} meters is equal to {feet} feet.")
    elif choice == '12':
        liters = float(input("Enter volume in liters: "))
        gallons = liters * 0.264172
        print(f"{liters} liters is equal to {gallons} gallons.")
    elif choice == '13':
        gallons = float(input("Enter volume in gallons: "))
        liters = gallons / 0.264172
        print(f"{gallons} gallons is equal to {liters} liters.")
    else:
        print("Invalid choice. Please try again.")

    repeat = input("Do you want to convert another unit? (yes/no): ")
    if repeat.lower() == "yes":
        unitconversion()
    else:
        print("Goodbye!")

unitconversion()
