import random

# Constants for the game
COLORS = ["R", "G", "B", "W", "Y", "O"]
TRIES = 10
CODELENGTH = 4

# Function to generate a random code
def codegenerate():
    code = []
    for _ in range(CODELENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code

# Function to get a guess from the user
def guesscode():
    while True:
        guess = input("Guess 4 colors (separated by spaces): ").upper().split()
        
        if len(guess) != CODELENGTH:
            print(f"You must guess exactly {CODELENGTH} colors.")
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. The valid colors are: {', '.join(COLORS)}. Try again.")
                break
        else:
            return guess

# Function to check the guessed code against the real code
def checkcode(guess, realcode):
    colorcounts = {}
    correctpos = 0
    incorrectpos = 0
    
    # Create a dictionary to count occurrences of each color in the real code
    for color in realcode:
        if color not in colorcounts:
            colorcounts[color] = 0
        colorcounts[color] += 1
        
    # Check for correct positions
    for guesscolor, realcolor in zip(guess, realcode):
        if guesscolor == realcolor:
            correctpos += 1
            colorcounts[guesscolor] -= 1
    
    # Check for incorrect positions, ignoring those already counted in correct positions
    for guesscolor, realcolor in zip(guess, realcode):
        if guesscolor != realcolor and guesscolor in colorcounts and colorcounts[guesscolor] > 0:
            incorrectpos += 1
            colorcounts[guesscolor] -= 1
    
    return correctpos, incorrectpos

# Main game function
def game():
    print(f"Welcome to CODE CRACKER! You have {TRIES} tries to guess the code.")
    print("The valid colors are:", ", ".join(COLORS))
    
    code = codegenerate()  # Generate the random code to guess
    for attempt in range(1, TRIES + 1):
        guess = guesscode()  # Get the user's guess
        correctpos, incorrectpos = checkcode(guess, code)  # Check the guess
        
        if correctpos == CODELENGTH:  # If the user guessed the entire code
            print(f"Congratulations! You guessed the code in {attempt} tries!")
            break
        
        # Provide feedback on the guess
        print(f"Attempt {attempt}: Correct positions: {correctpos}, Incorrect positions: {incorrectpos}")
    
    else:
        # If the user runs out of tries
        print("You've run out of tries. The correct code was:", " ".join(code))

# Run the game if this script is the main program
if __name__ == "__main__":
    game()
