def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    while True:
        number = input("Enter a number (or enter 'q' to quit): ")
        
        if number.lower() == 'q':
            break
        
        try:
            number = int(number)
            
            if number < 0:
                print("Factorial of negative number doesn't exist")
            else:
                result = factorial(number)
                print(f"Factorial of {number} is {result}")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
