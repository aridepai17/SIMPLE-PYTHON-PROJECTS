import random
from collections import Counter

# List of words (fruit names)
Words = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut Watermelon
cherry papaya berry peach litchi muskmelon plum kiwi avocado fig pomegranate pear 
dragonfruit custard jackfruit watermelon tangerine gooseberry mosambi'''

# Split words into a list and select a random word
Words = Words.split()
word = random.choice(Words)

# Main execution
if __name__ == '__main__':
    print("Guess the word! HINT: It's a name of a fruit.")

    # Initialize the display of the hidden word
    for _ in word:
        print('_', end=' ')
    print()

    # Game variables
    playing = True
    letterguessed = set()  # Store guessed letters
    chances = len(word) + 2  # Provide extra chances for longer words
    correct = 0
    flag = False  # Game win flag

    # Game loop
    while chances > 0 and not flag:
        print()
        chances -= 1

        guess = input('Enter a letter to guess: ').strip()  # Strip whitespace

        if not guess.isalpha():
            print('Enter only a LETTER.')
            continue
        elif len(guess) > 1:
            print('Enter only a SINGLE letter.')
            continue
        elif guess in letterguessed:
            print('You have already guessed that letter.')
            continue

        letterguessed.add(guess)  # Add the guess to guessed letters

        # Display the current state of the word
        correctguess = False
        for char in word:
            if char in letterguessed:
                print(char, end=' ')
                correctguess = True
            else:
                print('_', end=' ')

        print()  # Newline for next input

        # Check if all letters are guessed
        if set(word) <= letterguessed:
            print("The word is:", word)
            print("Congratulations, You won!")
            flag = True  # Set win flag

    # If the player lost
    if not flag:
        print("You lost! Try again.")
        print("The word was:", word)
