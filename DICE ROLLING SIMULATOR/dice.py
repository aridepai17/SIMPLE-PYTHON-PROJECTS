import random
def rolldice():
    number = random.randint(1, 6)
    print("You rolled: ", number)


def main():
    while True:
        print("1. Roll the dice")
        print("2. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            rolldice()
        elif choice == 2:
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()